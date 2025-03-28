import requests

class City:
    def __init__(self, name, latitude, longitude, units):
        self.name = name
        self.latitude = latitude
        self.longitude = longitude
        self.units = units
        self.get_data()
    
    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/3.0/onecall?units={self.units}&lat={self.latitude}&lon={self.longitude}&{API key}")

        except:
            print("No internet connection.")

        self.response_json = response.json()
        self.temp = self.response_json["current"]["temp"]
        self.sunrise = self.response_json["current"]["sunrise"]
        self.sunset = self.response_json["current"]["sunset"]
        self.feels_like = self.response_json["current"]["feels_like"]

    def temp_print(self):
        units_symbol = "C"
        if self.units == "imperial":
            units_symbol = "F"
        print(f"In Upper Marlboro it is currently {self.temp}{units_symbol}°")
        print(f"Sunrise is at {self.sunrise}")
        print(f"Sunset is at {self.sunset}")
        print(f"It feels like {self.feels_like}{units_symbol}°")

my_city = City("Upper Marlboro", 38.817169, -76.755630, units="imperial")
my_city.temp_print()    

vacation_city = City("Portland", 45.5152, -122.6784, units="imperial")
vacation_city.temp_print()

print(vacation_city.response_json)
# The above code defines a `City` class that fetches weather data from the OpenWeatherMap API for a given city based on its latitude and longitude.


