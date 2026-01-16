import requests
import json
import os
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice")
city_temp = input("Enter Your City Name = \n")
url = f"http://api.weatherapi.com/v1/current.json?key=fbd6820f68094d24bc6100720261501&q={city_temp}"
r = requests.get(url)
print(r.text)
wdic = json.loads(r.text)
print(wdic ["current"] ["temp_c"])

speaker.speak(f"The current temperature in {city_temp} is {wdic ['current'] ['temp_c']} degree Celsius")