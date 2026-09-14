slovar =  {"ključ" : "vrednost",
           "ključ2" : "vrednost2"}
print(type(slovar))
# dostop do tega
print(slovar["ključ"])

#raznoliki slovarji
razno = {"število" : 6,
          "ime" : "Luka",
          "seznam" : [1, 2, 3, 4],
          "slovar" : {"firma" : "Toyota", "moč" : "120kw"}}
print(razno["število"])
print(max(razno["seznam"]))
print(razno["slovar"]["firma"])
print(razno["slovar"]["moč"])


#open Meteo API
import requests
api = "https://api.open-meteo.com/v1/forecast?latitude=46.2299&longitude=14.36&daily=weather_code,rain_sum&hourly=temperature_2m&current=temperature_2m,is_day&timezone=Europe%2FBerlin"
call = requests.get(api).json()
print(call["daily"]["rain_sum"][0])