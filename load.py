from sqlalchemy import create_engine, text
import pandas as pd
from extract import get_weather
from transform import transform_weather

DB_URL = "postgresql://postgres:impala2006@localhost:5432/weather_db"

def get_or_create_city(engine, city_name, lat, lon):
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT city_id FROM dim_cities WHERE city_name = :name"),
            {"name": city_name}
        ).fetchone()

        if result:
            return result[0]

        insert_result = conn.execute(
            text("""INSERT INTO dim_cities (city_name, latitude, longitude) 
                    VALUES (:name, :lat, :lon) RETURNING city_id"""),
            {"name": city_name, "lat": lat, "lon": lon}
        ).fetchone()
        conn.commit()
        return insert_result[0]


def load_to_postgres(df, city_id):
    engine = create_engine(DB_URL)

    df["city_id"] = city_id

    df = df[["city_id", "temperature_c", "humidity", "wind_speed_kmh", "observation_time"]]

    df.to_sql(
        name="weather_facts",
        con=engine,
        if_exists="append",
        index=False
    )
    print(f"-> Данные загружены в weather_facts.")


def run_pipeline():
    print("Старт ETL")
    engine = create_engine(DB_URL)

    cities = {
        "Minsk": (53.9, 27.56),
        "Brest": (52.1, 23.7),
        "Gomel": (52.4, 31.0)
    }

    for city_name, (lat, lon) in cities.items():
        print(f"Обработка города: {city_name}...")

        raw = get_weather(lat, lon)
        if raw is None:
            continue

        city_id = get_or_create_city(engine, city_name, lat, lon)

        df = transform_weather(raw, city=city_name)

        load_to_postgres(df, city_id)

    print("ETL-процесс успешно завершен. Все данные загружены.")


if __name__ == "__main__":
    run_pipeline()