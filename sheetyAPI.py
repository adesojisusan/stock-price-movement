import requests
from datetime import datetime

API_ID = "1ba988ce"
API_KEY = "87bc5309f2d12de43203fc954e82e87b	"
natural_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint= "https://api.sheety.co/912f815324a829cddf6a015621389890/workoutTracking/workouts"

exercise_text = input("Tell me which exercises you did: ")

natural_headers ={
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"

}
natural_params ={
     "query":"ran 8 miles",
     "gender":"female",
     "weight_kg":72.5,
     "height_cm":167.64,
     "age":20
}

response = requests.post(url=natural_endpoint, json=natural_params, headers=natural_headers)
results= response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in results["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs)
    print(sheet_response.text)


