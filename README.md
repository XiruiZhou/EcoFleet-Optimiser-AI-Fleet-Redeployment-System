# 🚦 RPM Hire - AI Fleet & Equipment Optimization System

This repository contains a **Hackathon prototype** simulating RPM Hire’s AI-driven fleet & equipment management platform.  
The system integrates **mock data generation, demand forecasting, route optimization, equipment lifecycle management, dashboard visualization, and automated reporting**.

---

## 📂 Project Structure
├── data/ # Mock data (auto-generated)
│ ├── gps_data.csv # GPS logs (time, lat, lon, mileage, fuel)
│ ├── rental_history.csv # Historical rental data (state, equipment, count)
│ └── traffic_weather.json # Simulated traffic/weather API
│
├── src/
│ ├── data_pipeline.py # Generate mock data
│ ├── demand_model.py # Demand forecasting
│ ├── route_vrp.py # Route optimization (VRP with OR-Tools)
│ ├── lifecycle.py # Equipment lifecycle check
│ ├── dashboard.py # Streamlit dashboard
│ └── report.py # PDF report generator
│
├── app.py # Main script (runs the full pipeline)
├── requirements.txt # Python dependencies
└── README.md # Project documentation

---

## ⚙️ Installation
Clone the repository and install dependencies:
```
git clone https://github.com/<your-repo>/rpm-hire-ai.git
cd rpm-hire-ai
pip install -r requirements.txt
🚀 Usage
1. Run the full pipeline

python app.py
This will:

Generate mock GPS, rental, and weather data

Forecast equipment demand

Optimize vehicle route

Check equipment lifecycle

Output a sustainability report (data/report.pdf)

2. Launch the Dashboard

streamlit run src/dashboard.py
The dashboard shows:

📊 Demand forecast (bar chart by state)

🛣️ Optimal route

🔧 Equipment health status

⚖️ KPI customization sliders (cost / time / carbon)

📊 Example Outputs
data/gps_data.csv

python-repl
timestamp,latitude,longitude,mileage_km,fuel_L_per_100km
2025-09-29 12:00:00,-37.80,145.02,10,8.4
2025-09-29 12:05:00,-37.85,145.05,14,7.9
...
Dashboard (Streamlit)

Generated Report (data/report.pdf)
Includes:

Optimal route

Demand forecast

Equipment health status

🧩 Tech Stack
Python (pandas, numpy, plotly, matplotlib)

Google OR-Tools (VRP solver)

Streamlit (interactive dashboard)

fpdf2 (PDF reporting)

💡 Future Extensions
Integrate real GPS & IoT data instead of mock data

Connect to live weather/traffic APIs

Use ML models (LSTM, Prophet) for demand forecasting

Advanced Remaining Useful Life (RUL) prediction

Cross-company shared equipment pools

ESG-compliant sustainability reporting

👥 Team
Hackathon project for RPM Hire – Sustainable Fleet & Equipment Management
