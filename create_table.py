from sqlalchemy import create_engine, text

# Пароль impala2006
DB_URL = "postgresql://postgres:impala2006@localhost:5432/weather_db"

engine = create_engine(DB_URL)

drop_sql = "DROP TABLE IF EXISTS weather_data;"

create_dim_sql = """
CREATE TABLE IF NOT EXISTS dim_cities (
    city_id SERIAL PRIMARY KEY,
    city_name VARCHAR(100) UNIQUE NOT NULL,
    latitude FLOAT NOT NULL,
    longitude FLOAT NOT NULL
);
"""

create_fact_sql = """
CREATE TABLE IF NOT EXISTS weather_facts (
    fact_id SERIAL PRIMARY KEY,
    city_id INT REFERENCES dim_cities(city_id), -- Внешний ключ (Foreign Key)
    temperature_c FLOAT,
    humidity INT,
    wind_speed_kmh FLOAT,
    observation_time TIMESTAMP
);
"""

with engine.connect() as conn:
    print("Удаляем старую таблицу...")
    conn.execute(text(drop_sql))

    print("Создаем таблицу dim_cities (Измерения)...")
    conn.execute(text(create_dim_sql))

    print("Создаем таблицу weather_facts (Факты)...")
    conn.execute(text(create_fact_sql))

    conn.commit()
    print("Таблицы 'dim_cities' и 'weather_facts' успешно созданы.")