# src/shared_pool.py
import pandas as pd
import random

def generate_shared_pool(n=20):
    partners = ["PartnerA", "PartnerB", "PartnerC"]
    equipment = ["Barrier", "Sign", "LightTower", "MessageBoard"]

    rows = []
    for _ in range(n):
        rows.append({
            "partner_id": random.choice(partners),
            "equipment_type": random.choice(equipment),
            "status": random.choice(["Available", "In Use", "Maintenance"])
        })
    return pd.DataFrame(rows)

def load_shared_pool(path="data/shared_pool.csv"):
    return pd.read_csv(path)

if __name__ == "__main__":
    print(generate_shared_pool())
    print(load_shared_pool())
