# app.py
import os
import requests

class SimpleDb:
    def __init__(self, db_path):
        self.db_path = db_path

    def add_user(self, username):
        with open(self.db_path, "a") as f:
            f.write(f"{username}\n")

    def get_users(self):
        if not os.path.exists(self.db_path):
            return []
        with open(self.db_path, "r") as f:
            return [line.strip() for line in f.readlines()]
        
def get_weather_alert(city):
    # Zapytanie do API
    response = requests.get(f"https://api.weather.com/v1/{city}")
    data = response.json()

    if data.get("temp") > 30:
        return "Alarm - gorąco!"
    return "Pogoda w normie"
