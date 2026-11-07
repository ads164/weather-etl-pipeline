import pandas as pd

def transform_weather(raw_data: dict, city: str = "Minsk") -> pd.DataFrame:
    if not raw_data or "currentConditions" not in raw_data:
        raise ValueError("Пустые или некорректные данные от API")

    current = raw_data["currentConditions"]

    row = {
        "city": city,
        "temperature_c": current.get("temp"),
        "humidity": current.get("humidity"),
        "wind_speed_kmh": current.get("windspeed"),
        "observation_time": current.get("datetime"),
    }

    df = pd.DataFrame([row])

    df["observation_time"] = pd.to_datetime(df["observation_time"])
    df["temperature_c"] = pd.to_numeric(df["temperature_c"], errors='coerce').astype(float)

    df["humidity"] = pd.to_numeric(df["humidity"], errors='coerce').round().astype("Int64")

    df["wind_speed_kmh"] = pd.to_numeric(df["wind_speed_kmh"], errors='coerce').astype(float)

    print("Данные трансформированы:")
    print(df)
    return df

if __name__ == "__main__":
    from extract import get_weather
    raw = get_weather()
    df = transform_weather(raw)