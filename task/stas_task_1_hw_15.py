import requests


def city_weather(city_name=None):  # We wil pass city_name as key argument
    BASE_URL = 'http://api.openweathermap.org/data/2.5/weather?'  # Making some CONSTANTs
    API_KEY = 'd82759ebf4a4a5ed987117c4027b9dfa'
    complete_url = BASE_URL + "appid=" + API_KEY + "&q=" + city_name
    response = requests.get(complete_url)
    r_data = response.json()
    if r_data["cod"] != "404":
        y = r_data['main']
        current_t = y['temp']
        current_p = y["pressure"]
        z = r_data["weather"]
        weather_description = z[0]["description"]
        return str((round(current_t - 273.15))), str(current_p)
    else:
        return 'city not found'


if __name__ == '__main__':
    print(city_weather(city_name=input('Enter your city'))) #Cover result of function in print to display result
