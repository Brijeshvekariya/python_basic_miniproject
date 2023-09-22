import requests
import json
import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
name = input("Enter your name : ")

city = input("Enter your city : ")

url = f"http://api.weatherapi.com/v1/current.json?key=2edddd748e394a3a92862438232209&q={city}"
r = requests.get(url)
# print((r.text))

weather = json.loads(r.text)
# print(type(weather))
# print(weather)
# speaker.Speak(f"Hello {name}")

    
    
# print(weather["current"])
w_c = weather["current"]["temp_c"]
# w_f = weather["current"]["temp_f"]
# print(f"The Current weather in {city} is : {w_c}")
# print(f"The Current weather in {city} is : {w_f}")
speaker.Speak(f"Hello {name} , The Current weather in {city} is : {w_c} degeree Celsius")

