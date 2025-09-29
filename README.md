# 🚦 RPM Hire - AI Fleet & Equipment Optimization System

This project is a **Hackathon prototype** simulating RPM Hire’s AI-driven fleet & equipment management platform.  
It integrates **mock data generation, demand forecasting, route optimization, equipment lifecycle management, dashboard visualization, and automated reporting**.

---

## 📂 Project Structure
├── data/ # Mock data (auto-generated)
│ ├── gps_data.csv
│ ├── rental_history.csv
│ └── traffic_weather.json
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
├── requirements.txt # Dependencies
└── README.md

yaml
複製程式碼

---

## ⚙️ Installation
```bash
git clone https://github.com/<your-repo>/rpm-hire-ai.git
cd rpm-hire-ai
pip install -r requirements.txt
🚀 Usage
1. Run full pipeline
bash
複製程式碼
python app.py
This will:

Generate mock GPS, rental, and weather data

Forecast equipment demand

Optimize vehicle route

Check equipment lifecycle

Output a sustainability report (data/report.pdf)

2. Launch Dashboard
bash
複製程式碼
streamlit run src/dashboard.py
The dashboard shows:

Demand forecast (bar chart)

Optimal route

Equipment health status

KPI customization sliders

📊 Example Output
data/gps_data.csv: Simulated GPS logs

data/rental_history.csv: State-wise rental frequency

data/traffic_weather.json: Mock API data

data/report.pdf: Auto-generated sustainability report

🧩 Tech Stack
Python (pandas, numpy, matplotlib, plotly, scikit-learn)

Google OR-Tools (VRP solver)

Streamlit (dashboard)

fpdf2 (PDF report)

💡 Future Extensions
Integrate real GPS API & weather/traffic APIs

Train ML models for demand forecasting (LSTM, Prophet)

Real-time lifecycle prediction (Remaining Useful Life - RUL)

Multi-company shared equipment pools

ESG-compliant sustainability reporting

👥 Team
Hackathon project for RPM Hire – Sustainable Fleet & Equipment Management.

yaml
複製程式碼
