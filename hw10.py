import requests
from hw10_1 import save_temperature

# Координати міста
CITY_LAT = 48.7833
CITY_LON = 33.2333
WEATHER_API_URL = f'https://api.open-meteo.com/v1/forecast?latitude={CITY_LAT}&longitude={CITY_LON}&current_weather=true'

# Отримання температури
def get_temperature():
    try:
        response = requests.get(WEATHER_API_URL)
        data = response.json()
        return data['current_weather']['temperature']
    except Exception as e:
        print(f"Помилка отримання погоди: {e}")
        return None

# Оновлення даних
def update_weather_data():
    temp = get_temperature()
    if temp is not None:
        save_temperature(temp)
        print(f"Оновлено: {temp}°C")
