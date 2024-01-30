import requests
api_key = ""
OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat":28.644800,
    "lon":77.216721,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()
data = response.json()
# res = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat=28.644800&lon=77.216721&appid={api_key}")
# res.raise_for_status()
# dat = res.json()
# print(dat)
# print(data)
for i in range(4):
    if (data["list"][i]["weather"][0]["id"]) <700:
        print("may rain",data["list"][i]["weather"][0]["description"])
    else:
        print("no rain",data["list"][i]["weather"][0]["description"])