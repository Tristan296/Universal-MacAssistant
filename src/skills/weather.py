import requests
import os
import sys

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

from extras.loading_logo import Loader
from core.voice_assistant import VoiceAssistant

class Weather:
    def __init__(self, voice_assistant, choice):
        self.voice_assistant = voice_assistant
        self.choice = choice
        
    def run(self):
        while True:
            self.voice_assistant.speak("Choose one of the following weather metrics")
            prompt = """
            Available weather metrics:
                1. Temperature
                2. Feels Like Temperature
                3. Humidity
                4. Rainfall
                5. Snowfall
                6. Air Pressure
                7. Wind
            """
            print(prompt)
            self.choice = self.voice_assistant.listen().lower()
            city_name = self.get_city_name()
            self.find_weather(city_name)
            break
    
    def get_temperature(self, data):
        temperature = round((data["main"]["temp"] - 273.15), 1) # convert from kelvin to celsius
        return temperature
        
    def feels_like(self, data):
        feels_like_temp = round((data["main"]["feels-like"] - 273.15), 1) # convert from kelvin to celsius
        return feels_like_temp
    
    def get_humidity(self, data):
        humidity = data["main"]["humidity"]
        return humidity
    
    def wind(self, data):
        wind_speed = round((data["wind"]["speed"] * 1.94384), 2) # convert from m/s to knots
        return wind_speed
    
    def pressure(self, data):
        pressure = data["main"]["pressure"]
        return pressure
    
    def rainfall(self, data):
        while True:
            rainfall_prompt = "Did you want the rainfall over the one hour or the past 3 hours?"
            self.voice_assistant.speak(rainfall_prompt)
            rainfall_option = self.voice_assistant.listen().lower()
            if "one" in rainfall_option:
                past_hour_rainfall = data["rain"]["1h"]
                past_hour_rainfall_text = "The rainfall over the past hour was ", past_hour_rainfall, "millilitres."
                return past_hour_rainfall_text
            
            elif "three" in rainfall_option:
                past_three_hours_rainfall = data["rain"]["3h"]
                past_three_hours_rainfall_text = "The rainfall over the past three hours was ", past_three_hours_rainfall, "millilitres."
                return past_three_hours_rainfall_text
            else:
                print("Please choose either past 1hr or past 3hrs")

    def get_city_name(self):
        city_prompt = "Enter city name: "
        print(city_prompt)
        self.voice_assistant.speak(city_prompt)
        chosen_city = self.voice_assistant.listen().lower()
        return chosen_city

    def find_weather(self, city_name):
        api_key = "73e9748c0e68dc34e3ae90236f82d642"
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}"

        try:
            # JSON HTTP Request
            response = requests.get(url)
            data = response.json()
            
            # Response successful
            if response.status_code == 200:
                if "temperature" in self.choice:
                    temp = self.get_temperature(data)
                    temp_text = f"The current temperature in {city_name} is {temp} degrees celcius."
                    print(temp_text)
                    self.voice_assistant.speak(temp_text)
                    
                elif "feels like" in self.choice and "temperature" in self.choice:
                    feels_like_temp = self.feels_like(data)
                    print(feels_like_temp + " degrees celsius")
                    self.voice_assistant.speak(f"The feels like temperature in {city_name} is {feels_like_temp} degrees celcius.")
                    
                elif "rainfall" in self.choice:
                    past_rain = self.rainfall(data)
                    print(past_rain)
                    self.voice_assistant.speak(past_rain)
                
                elif "pressure" in self.choice:
                    pressure = self.pressure(data)
                    print(pressure)    
                    
                elif "wind" in self.choice:
                    wind_speed = self.wind(data)
                    print(wind_speed)
            
            else:
                print("Failed to retrieve weather data.")
        except requests.exceptions.RequestException as e:
            print("An error occurred:", str(e))


if __name__ == "__main__":
    voice_assistant = VoiceAssistant()
    weather = Weather(voice_assistant, "")
    weather.run()