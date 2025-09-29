# src/dashboard.py
import streamlit as st
import pandas as pd
import plotly.express as px
from demand_model import forecast_demand
from route_vrp import solve_vrp
from lifecycle import check_equipment_health

st.title("RPM Hire - AI Fleet & Equipment Dashboard")

# Demand Forecast
st.header(" Demand Forecast")
df_forecast = forecast_demand()
st.dataframe(df_forecast)

fig = px.bar(df_forecast, x="state", y="forecast_demand", color="state", title="Forecasted Equipment Demand")
st.plotly_chart(fig)

# Route Optimization
st.header(" Route Optimization")
route = solve_vrp()
st.write("Optimal route:", route)

# Equipment Health
st.header(" Equipment Health Status")
status = check_equipment_health()
st.write(status)

# KPI Customization
st.header("KPI Customization")
weight_cost = st.slider("Weight: Cost", 0, 100, 30)
weight_time = st.slider("Weight: Time", 0, 100, 40)
weight_carbon = st.slider("Weight: Carbon", 0, 100, 30)
st.write(f"Selected KPI Weights → Cost: {weight_cost}, Time: {weight_time}, Carbon: {weight_carbon}")
