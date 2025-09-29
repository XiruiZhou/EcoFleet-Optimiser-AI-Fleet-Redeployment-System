# src/lifecycle.py
import pandas as pd

def check_equipment_health(gps_path="data/gps_data.csv", threshold_km=200):
    df = pd.read_csv(gps_path)
    last_mileage = df["mileage_km"].iloc[-1]
    if last_mileage > threshold_km:
        return "⚠️ Maintenance required"
    return "✅ Equipment OK"

if __name__ == "__main__":
    print(check_equipment_health())
