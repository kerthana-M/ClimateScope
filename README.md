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
|		└── weather_cleaned_with_seasons.csv
│
├── notebooks/
│   └── 01_data_preparation.ipynb
│   └── 02_analysis.ipynb
|
├── dashboard/
│   └── app.py
|
├── reports/
│   └── milestone1_summary.pdf
|   └── milestone2_summary.pdf
│   └── milestone3_summary.pdf
|   └── dashboard_wireframe.pdf
|  
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

## Milestone 1: Data Preprocessing

Objectives achieved:

- Loaded and inspected the Global Weather dataset
- Handled missing values:
- Numerical → column mean
- Categorical → "Unknown"
- Converted timestamps and extracted year/month
- Validated data ranges and consistency
- Saved cleaned dataset for reuse
----
## Milestone 2: Core Analysis & Visualization Design
### Statistical & Seasonal Analysis

- Monthly aggregation by country, year, and month
- Seasonal classification (Winter, Spring, Summer, Autumn)
- Analysis of:
      - Temperature trends
  	  -	Precipitation patterns
	  - Wind speed and pressure relationships
	  - Seasonal variability across regions

### Exploratory Visualizations
- Temperature distribution
- Monthly temperature trends
- Precipitation distribution
- Seasonal temperature comparison (country-wise)
- These visualizations validate data quality and reveal meaningful climate patterns.

## Dashboard Wireframe Design

A dashboard layout (wireframe) was designed to guide future implementation.

### Planned Dashboard Sections

#### Global Overview

- Line chart: Global temperature trend
- KPI cards: Avg temperature, humidity, rainfall

#### Seasonal Analysis
- Country selector (dropdown)
- Bar chart: Seasonal temperature
- Line chart: Seasonal precipitation

#### Regional Comparison

- Choropleth map: Average temperature
- Bar chart: Wind speed by region

#### Extreme Events

- Scatter plot: Extreme temperature & precipitation
- Filters: Year, country

### 📄 Wireframe available at:

#### reports/dashboard_wireframe.pdf
----
## Milestone 3: Visualization Development & Interactivity
Features Implemented:
- Interactive dashboard using Streamlit
- Dynamic filters (country, year, season)
- Metric selection for flexible analysis
- Multiple visualization types:
- Line charts (trends)
- Bar charts (seasonal patterns)
- Choropleth maps (regional comparison)
- Scatter plots (extreme events)
- Heatmaps (correlation)
- Insight annotations for each section
----

## How to Run the Dashboard
```
pip install -r requirements.txt
streamlit run dashboard/app.py
```
----

## Next Steps
- Perform final testing and optimization
- Prepare comprehensive final report
- Deploy dashboard (optional)
- Add advanced features for future enhancement

