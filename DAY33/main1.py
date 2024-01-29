import requests

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()

# data = response.json()
# print(data['iss_position']['latitude'])
# print(data['iss_position']['longitude'])

parameters = {'lat':26.44992,'lng':80.331871,'formatted':0}
response = requests.get(url="https://api.sunrise-sunset.org/json",params=parameters)
response.raise_for_status()
data = response.json()
# print(data)
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)
print(sunset)
print((sunrise.split('T')[1]).split('+')[0])
print((sunset.split('T')[1]).split('+')[0])