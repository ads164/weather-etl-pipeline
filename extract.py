import requests


def get_weather(lat=53.9, lon=27.56):
    # Координаты Минска по умолчанию
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lat},{lon}"
    params = {
        "unitGroup": "metric",
        "include": "current",
        "elements": "datetime,temp,humidity,windspeed",
        "contentType": "json"
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        print("Данные успешно получены!")
        return response.json()
    else:
        print(f"Ошибка: {response.status_code}")
        return None


if __name__ == "__main__":
    data = get_weather()
    print(data)