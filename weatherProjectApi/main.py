import requests

cityName = input("Renseigner le nom de la ville : ")

language = "fr"
key = "f93db5cbad569ad0793548e103f05ef3"
api_link = f"https://api.openweathermap.org/data/2.5/weather?q={cityName}&appid={key}&lang={language}"


json = requests.get(api_link).json()
JSON = json['weather'][0]['description']

print(JSON)