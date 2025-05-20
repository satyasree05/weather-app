import tkinter as tk
import requests

# Replace with your actual OpenWeatherMap API key
API_KEY = "ab3b22962923ff27f1cc1695b5dbdc53"

def get_weather():
    city = city_entry.get().strip()
    if not city:
        result_label.config(text="Please enter a city name.")
        return

    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    data = response.json()

    if data.get("cod") != 200:
        error_message = data.get("message", "City not found. Try again.")
        result_label.config(text=error_message.capitalize())
    else:
        weather = data["weather"][0]["description"].title()
        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]

        result = (f"City: {city.title()}\n"
                  f"Weather: {weather}\n"
                  f"Temperature: {temp}°C\n"
                  f"Humidity: {humidity}%\n"
                  f"Wind Speed: {wind_speed} m/s")
        result_label.config(text=result)

# GUI Setup
window = tk.Tk()
window.title("Weather App")
window.geometry("300x250")

tk.Label(window, text="Enter City Name:", font=("Arial", 12)).pack(pady=10)
city_entry = tk.Entry(window, font=("Arial", 12))
city_entry.pack()

tk.Button(window, text="Get Weather", command=get_weather, font=("Arial", 12)).pack(pady=10)
result_label = tk.Label(window, text="", font=("Arial", 12), justify="left")
result_label.pack(pady=10)

window.mainloop()
