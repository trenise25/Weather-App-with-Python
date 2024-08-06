import requests

api_key = '4a66133573c373c68993aaca20f4615b'
user_input = input("Enter your city: ")
weather_data = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

if weather_data.json()['cod'] == '404':
    print("No City Found")
else:
    weather = weather_data.json()['weather'][0]['main']
    temp = round(weather_data.json()['main']['temp'])
    
print(f"The weather in {user_input} is: {weather}")
print(f"The temperature in {user_input} is: {temp}ºF")