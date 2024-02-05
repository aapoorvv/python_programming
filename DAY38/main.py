import requests
from datetime import datetime
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
API_KEY = ""
API_ID = ""
GENDER = "male"
WEIGHT_KG = "50"
HEIGHT_CM = "200"
AGE = "99"

header = {
    'x-app-id':API_ID,
    'x-app-key':API_KEY,
    "x-remote-user-id": "0"
}
user_input = str(input())
user_params = {
    "query":user_input,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE}
response = requests.post(url = exercise_endpoint, json=user_params,headers=header)
result = response.json()
print(result)

today = datetime.now()
date = today.strftime("%d/%m/%Y")
time = today.strftime("%H:%M:%S")
exercise = result['exercises'][0]['name']
duration = result['exercises'][0]['duration_min']
calories = result['exercises'][0]['nf_calories']

sheety_endpoint = "https://api.sheety.co/332c645f8020354dff8df75228994f45/myWorkouts/workouts"
sheety_inputs = {'workout':{
    'date':date,
    'time':time,	
    'exercise':exercise,	
    'duration':duration,	
    'calories':calories
}}
sheety_headers = {"Authorization":""}
sheet_response = requests.post(
    url = sheety_endpoint, 
    json=sheety_inputs,
    headers=sheety_headers)
print(sheet_response.text)