# src/demand_model.py
import pandas as pd

def forecast_demand(rental_history_path="data/rental_history.csv"):
    df = pd.read_csv(rental_history_path)
    forecast = df.groupby("state")["count"].sum().reset_index()
    forecast.rename(columns={"count": "forecast_demand"}, inplace=True)
    return forecast

if __name__ == "__main__":
    print(forecast_demand())
