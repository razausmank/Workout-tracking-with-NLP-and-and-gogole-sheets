import requests
from datetime import datetime as d

APP_ID = 'daf08ac2'
APP_KEY = '5f98f5d8c55ad8caaea2c3382f1dd318'
BASE_URL = "https://trackapi.nutritionix.com"
EXERCISE_URL = "/v2/natural/exercise"
SHEET_URL = "https://api.sheety.co/cdc00878773b89756231d9ed724df698/myWorkouts/workouts"

headers = {
    'x-app-id': APP_ID,
    'x-app-key': APP_KEY,
    'Content-Type': 'application/json'
}

params = {
    "query": "i played football for an hour"
}
response = requests.post(url=f"{BASE_URL}{EXERCISE_URL}", json=params, headers=headers)

exercises = response.json()["exercises"][0]

print(exercises);

params = {
    'workout': {
        "date": d.today().strftime("%d/%m/%Y"),
        "time": d.now().strftime("%H:%M:%S"),
        "exercise":  exercises["name"].title(),
        "duration": exercises["duration_min"],
        "calories": exercises["nf_calories"],

    }
}
sheet_response = requests.post(url=SHEET_URL, json=params)

print(sheet_response.text, sheet_response.status_code)

"""
let url = 'https://api.sheety.co/cdc00878773b89756231d9ed724df698/myWorkouts/workouts';
  let body = {
    workout: {
      "Exercise" : 'something'
    }
  }
  fetch(url, {
    method: 'POST',
    body: JSON.stringify(body)
  })
  .then((response) => response.json())
  .then(json => {
    // Do something with object
    console.log(json.workout);
  });
"""
