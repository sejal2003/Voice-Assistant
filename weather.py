import requests

api_address = 'https://api.openweathermap.org/data/2.5/weather?q=Gwalior&appid=14851c80360ade07d051285faa23734f'
json_data = requests.get(api_address).json()

def temp():
    temperature = round(json_data["main"]["temp"]-273, 1)
    return temperature

def des():
    description = json_data["weather"][0]["description"]
    return description

