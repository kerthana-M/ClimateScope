# ClimateScope 
Visualizing Global Weather Trends and Extreme Events

## Project Overview
ClimateScope is a data analytics and visualization project focused on exploring global weather patterns and extreme weather events using real-world, daily-updated data. The project transforms raw weather data into meaningful insights through structured preprocessing, exploratory analysis, and interactive visualizations.The project also includes seasonal classification of weather data to analyze and visualize country-wise seasonal temperature and precipitation patterns.

By leveraging the Global Weather Repository dataset, ClimateScope enables users to:

- Analyze seasonal and regional weather trends
- Compare climate conditions across countries
- Identify anomalies and extreme weather behavior
- Interact with data through visual dashboards
----
## Project Objectives
- Analyze global weather patterns over time
- Identify seasonal trends and regional variations
- Detect extreme weather conditions
- Present insights using interactive and intuitive visualizations
- Build a scalable foundation for future predictive analysis
----
## Dataset
- Name: Global Weather Repository
- Source: Kaggle
- Records: 125,501
- Features: 41
- Coverage: Global
- Update Frequency: Daily
The dataset includes:
	- Weather parameters (temperature, humidity, wind, precipitation, pressure)
	- Air quality indicators (PM2.5, PM10, CO, NO₂, O₃, SO₂)
  - Astronomical data (sunrise, sunset, moon phase)
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
## Tech Stack
- Programming Language
	- Python 3
- Libraries & Tools
	- pandas – data cleaning and transformation
	- numpy – numerical computations
	- matplotlib / seaborn – exploratory data analysis (EDA)
	- Plotly – interactive visualizations
	- Streamlit – dashboard development
	- Kaggle API – dataset access
----
## Project Workflow
### Data Acquisition
- Dataset downloaded using Kaggle API
- Raw data stored separately to preserve original source
### Data Understanding & Exploration
- Schema inspection and data type validation
- Identification of key weather, air quality, and time-based variables
### Data Cleaning & Preprocessing
- Duplicate removal
- Retention of epoch-based timestamps for temporal consistency
- conversion of epoch time to datetime
- unit standardization (Celsius, km/h, mm)
- Feature selection and column renaming
- Extracted year and month from datetime values
- Created a new categorical feature `season` by mapping months to climatological seasons (Winter, Spring, Summer, Autumn)
### Data Aggregation
- Aggregation from timestamp-level data to monthly averages
- Grouped by country, year, and month
## Season Identification & Analysis

To support seasonal climate analysis, each monthly observation was assigned a climatological season based on its month:
- Winter: December – February
- Spring: March – May
- Summer: June – August
- Autumn: September – November

This seasonal classification enables country-wise comparison of temperature and precipitation patterns across different periods of the year.
### Exploratory Data Analysis (EDA)
- Temperature distribution analysis
- Monthly temperature trend visualization
- Precipitation distribution analysis
- Data quality validation through visual checks
----
## Current Status
Milestone 1 Completed
#### Milestone 1 Deliverables:
- Cleaned and processed dataset
- Data quality validation
- Initial EDA plots
- Milestone 1 summary report

## Future Enhancements
- Interactive dashboard using Streamlit
- Choropleth maps for geographic analysis
- Extreme weather detection and anomaly analysis
- Predictive modeling for weather trends
- Live API-based weather updates





