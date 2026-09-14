import requests

def vreme(lat, lon):
	params = {"latitude": lat, "longitude": lon, "current": "temperature_2m",
			  "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum,wind_speed_10m_max",
			  "forecast_days": 7, "timezone": "Europe/Ljubljana"}
	return requests.get("https://api.open-meteo.com/v1/forecast", params=params).json()


mesto = input("Mesto: ")
geo = requests.get("https://geocoding-api.open-meteo.com/v1/search",
				   params={"name": mesto, "count": 1, "language": "sl"}).json()["results"][0]
data = vreme(geo["latitude"], geo["longitude"])
d = data["daily"]

print(f"\n{geo['name']}: trenutno {data['current']['temperature_2m']} °C")
for i, datum in enumerate(d["time"]):
	print(datum, f"{d['temperature_2m_min'][i]} - {d['temperature_2m_max'][i]} °C")

najtop = max(range(7), key=lambda i: d["temperature_2m_max"][i])
najhlad = min(range(7), key=lambda i: d["temperature_2m_min"][i])
najrazlika = max(range(7), key=lambda i: d["temperature_2m_max"][i] - d["temperature_2m_min"][i])
print(f"Najtoplejši: {d['time'][najtop]}, {d['temperature_2m_max'][najtop]} °C")
print(f"Najhladnejši: {d['time'][najhlad]}, {d['temperature_2m_min'][najhlad]} °C")
razlika = d["temperature_2m_max"][najrazlika] - d["temperature_2m_min"][najrazlika]
print(f"Največja razlika: {d['time'][najrazlika]}, {razlika:.1f} °C")

mesta = {"Ljubljana": (46.0569, 14.5058), "Maribor": (46.5547, 15.6459),
		 "Kranj": (46.2389, 14.3556), "Celje": (46.2364, 15.2677),
		 "Koper": (45.5481, 13.7302), "Velenje": (46.3592, 15.1103),
		 "Novo mesto": (45.8039, 15.1689), "Ptuj": (46.4194, 15.8697),
		 "Trbovlje": (46.1547, 15.0456), "Kamnik": (46.2259, 14.6121)}
napoved = {ime: vreme(*koordinate)["daily"] for ime, koordinate in mesta.items()}

def izpisi(opis, kljuc):
	for beseda, izbira in (("najmanj", min), ("največ", max)):
		ime = izbira(napoved, key=lambda x: napoved[x][kljuc][0])
		enota = "mm" if kljuc == "precipitation_sum" else "km/h" if kljuc == "wind_speed_10m_max" else "°C"
		print(f"{opis} ({beseda}): {ime}, {napoved[ime][kljuc][0]} {enota}")

izpisi("Temperatura", "temperature_2m_max")
izpisi("Dež", "precipitation_sum")
izpisi("Veter", "wind_speed_10m_max")
 