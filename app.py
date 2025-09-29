# app.py
from src.data_pipeline import generate_gps_data, generate_rental_history, generate_weather_traffic
from src.demand_model import forecast_demand
from src.route_vrp import solve_vrp
from src.lifecycle import check_equipment_health
from src.report import generate_report

print(" Running RPM Hire AI System Prototype...")

# Step 1: Generate mock data
generate_gps_data()
generate_rental_history()
generate_weather_traffic()

# Step 2: Demand forecast
demand = forecast_demand()
print("Demand Forecast:\n", demand)

# Step 3: Route optimization
route = solve_vrp()
print("Optimal Route:", route)

# Step 4: Equipment health
health = check_equipment_health()
print("Equipment Health:", health)

# Step 5: Report
report_path = generate_report(route, demand, health)
print("Report saved at:", report_path)

print("All modules executed successfully.")
