import requests

city=input("Gimme the city: ")
url='http://api.weatherapi.com/v1/current.json?key=862514c557c54130b9f141705231208&q='+city+'&aqi=no'
response=requests.get(url)
weather_json = response.json()

temp=weather_json.get('current').get('temp_c')
condition=weather_json.get('current').get('condition').get('text')

print("Today's weather in",city,"is",condition,"and the temperature is", temp,"degrees")