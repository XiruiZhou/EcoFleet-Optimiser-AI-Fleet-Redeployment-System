# src/data_pipeline.py
import pandas as pd
import numpy as np
import json
from datetime import datetime, timedelta

def generate_gps_data(num_points=100):
    np.random.seed(42)
    timestamps = [datetime.now() - timedelta(minutes=i*5) for i in range(num_points)]
    lat = np.random.uniform(-37.9, -37.7, num_points)  
    lon = np.random.uniform(144.9, 145.1, num_points) 
    mileage = np.cumsum(np.random.randint(1, 5, num_points))
    fuel = np.random.uniform(6, 12, num_points)  
    df = pd.DataFrame({
        "timestamp": timestamps,
        "latitude": lat,
        "longitude": lon,
        "mileage_km": mileage,
        "fuel_L_per_100km": fuel
    })
    df.to_csv("data/gps_data.csv", index=False)

def generate_rental_history():
    states = ["VIC", "NSW", "QLD"]
    equipment = ["Barrier", "Sign", "Light Tower"]
    records = []

    for state in states:
        for eq in equipment:
            records.append({
                "state": state,
                "equipment": eq,
                "count": np.random.randint(50, 200)
            })

    df = pd.DataFrame(records)
    df.to_csv("data/rental_history.csv", index=False)

def generate_weather_traffic():
    data = {
        "traffic": np.random.randint(50, 500),
        "weather": np.random.choice(["sunny", "rainy", "windy"])
    }
    with open("data/traffic_weather.json", "w") as f:
        json.dump(data, f)

if __name__ == "__main__":
    generate_gps_data()
    generate_rental_history()
    generate_weather_traffic()
    print("Mock data generated in /data folder.")
