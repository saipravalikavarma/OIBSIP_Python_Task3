import requests

API_KEY = "enter weather API key"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            city_name = data["name"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            weather_condition = data["weather"][0]["description"]

            print("\n--- Weather Information ---")
            print(f"City: {city_name}")
            print(f"Temperature: {temperature} °C")
            print(f"Humidity: {humidity}%")
            print(f"Condition: {weather_condition}")
        else:
            print("\nCity not found. Please enter a valid city name.")

    except Exception as e:
        print("\nError occurred:", e)


print("=== Basic Weather App ===")
city = input("Enter city name: ")
get_weather(city)
