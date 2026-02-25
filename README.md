# ClimateScope 
Visualizing Global Weather Trends and Extreme Events

## Project Overview
ClimateScope is a data analytics and visualization project focused on exploring global weather patterns and extreme weather events using real-world, daily-updated data. The project transforms raw weather data into meaningful insights through structured preprocessing, exploratory analysis, and interactive visualizations.

By leveraging the Global Weather Repository dataset, ClimateScope enables users to:

- Analyze seasonal and regional weather trends
- Compare climate conditions across countries
- Identify anomalies and extreme weather behavior
- Interact with data through visual dashboards

## Project Objectives


## Dataset
- Source: :contentReference[oaicite:0]{index=0}
- Dataset Name: Global Weather Repository
- Access Method: Kaggle Python API
- Note: Raw dataset files are not included in this repository

----
## Project Structure
```
ClimateScope/
│
├── data/
│   ├── raw/                # Original dataset (unchanged)
│   └── processed/          # Cleaned & aggregated dataset
│       └── weather_cleaned.csv
│
├── notebooks/
│   └── 01_data_preparation.ipynb
│
├── reports/
│   └── milestone1_summary.md
│
├── README.md
└── requirements.txt
```
----
## Environment Setup (Windows)

### 1. Clone the Repository
```bash
git clone https://github.com/<your-username>/ClimateScope.git
cd ClimateScope
