import pandas as pd
import streamlit as st
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="ClimateScope Dashboard", layout="wide")

st.title("🌍 ClimateScope Dashboard")
st.caption("Interactive dashboard for analyzing global climate patterns and extreme weather events")

# -----------------------------
# LOAD DATA
# -----------------------------
df = pd.read_csv("data/processed/weather_cleaned_with_seasons.csv")

# -----------------------------
# SIDEBAR
# -----------------------------
st.sidebar.title("🌍 ClimateScope Controls")

countries = st.sidebar.multiselect(
    "Select Country(s)",
    options=sorted(df["country"].unique()),
    default=[df["country"].unique()[0]]
)

year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["year"].min()),
    int(df["year"].max()),
    (int(df["year"].min()), int(df["year"].max()))
)

seasons = st.sidebar.multiselect(
    "Select Season",
    options=df["season"].unique(),
    default=df["season"].unique()
)

metric = st.sidebar.selectbox(
    "Select Metric",
    ["temperature_celsius", "humidity", "precip_mm", "wind_kph"]
)

top_n = st.sidebar.slider("Top N Countries", 5, 20, 10)

# -----------------------------
# FILTER DATA
# -----------------------------
filtered_df = df[
    (df["country"].isin(countries)) &
    (df["year"].between(year_range[0], year_range[1])) &
    (df["season"].isin(seasons))
]

# -----------------------------
# KPI SECTION
# -----------------------------
st.subheader("🌍 Global Climate Summary")

col1, col2, col3 = st.columns(3)

col1.metric("Avg Temperature (°C)", round(filtered_df["temperature_celsius"].mean(), 2))
col2.metric("Avg Humidity (%)", round(filtered_df["humidity"].mean(), 2))
col3.metric("Avg Rainfall (mm)", round(filtered_df["precip_mm"].mean(), 2))

st.markdown("---")

# -----------------------------
# TABS
# -----------------------------
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "📈 Trends",
    "🌦 Seasonal",
    "🌍 Regional",
    "⚡ Extremes",
    "📊 Distribution"
])

# -----------------------------
# 📈 TRENDS
# -----------------------------
with tab1:
    st.subheader("📈 Climate Trends Over Time")

    global_trend = df.groupby("year")[metric].mean().reset_index()

    fig1 = px.line(global_trend, x="year", y=metric, markers=True,
                   title=f"{metric} Trend")

    st.plotly_chart(fig1, use_container_width=True)

    st.info("📌 Insight: Long-term trends indicate gradual climate variation and possible warming patterns.")

# -----------------------------
# 🌦 SEASONAL
# -----------------------------
with tab2:
    st.subheader("🌦 Seasonal Climate Patterns")

    col4, col5 = st.columns(2)

    seasonal_temp = filtered_df.groupby("season")["temperature_celsius"].mean().reset_index()

    fig2 = px.bar(seasonal_temp, x="season", y="temperature_celsius",
                  title="🌡 Seasonal Temperature Patterns")

    col4.plotly_chart(fig2, use_container_width=True)

    seasonal_precip = filtered_df.groupby("season")["precip_mm"].mean().reset_index()

    fig3 = px.line(seasonal_precip, x="season", y="precip_mm",
                   markers=True, title="🌧 Seasonal Precipitation Trends")

    col5.plotly_chart(fig3, use_container_width=True)

    st.info("📌 Insight: Seasonal cycles strongly influence temperature and precipitation patterns.")

# -----------------------------
# 🌍 REGIONAL
# -----------------------------
with tab3:
    st.subheader("🌍 Regional Climate Comparison")

    country_compare = df.groupby("country")[metric].mean().reset_index() \
                        .sort_values(by=metric, ascending=False).head(top_n)

    fig_map = px.choropleth(
        country_compare,
        locations="country",
        locationmode="country names",
        color=metric,
        title=f"Global {metric} Distribution"
    )

    st.plotly_chart(fig_map, use_container_width=True)

    fig_country = px.bar(
        country_compare,
        x="country",
        y=metric,
        title=f"Top {top_n} Countries by {metric}"
    )

    st.plotly_chart(fig_country, use_container_width=True)

    fig4 = px.scatter(
        filtered_df,
        x="pressure_mb",
        y="wind_kph",
        color="temperature_celsius",
        title="Wind Speed vs Pressure"
    )

    st.plotly_chart(fig4, use_container_width=True)

    st.info("📌 Insight: Regional differences highlight diverse climate behaviors across countries.")

# -----------------------------
# ⚡ EXTREMES
# -----------------------------
with tab4:
    st.subheader("⚡ Extreme Weather Events")

    extreme_temp = df[df["temperature_celsius"] > df["temperature_celsius"].quantile(0.95)]
    extreme_rain = df[df["precip_mm"] > df["precip_mm"].quantile(0.95)]

    col6, col7 = st.columns(2)

    fig5 = px.scatter(extreme_temp, x="temperature_celsius", y="humidity",
                      title="🔥 Extreme Temperature Events")

    col6.plotly_chart(fig5, use_container_width=True)

    fig6 = px.scatter(extreme_rain, x="precip_mm", y="humidity",
                      title="🌧 Extreme Rainfall Events")

    col7.plotly_chart(fig6, use_container_width=True)

    st.info("📌 Insight: Extreme events are rare but critical indicators of climate risk.")

# -----------------------------
# 📊 DISTRIBUTION
# -----------------------------
with tab5:
    st.subheader("📊 Data Distribution Analysis")

    col8, col9 = st.columns(2)

    fig_hist1 = px.histogram(df, x="temperature_celsius",
                             title="🌡 Temperature Distribution")

    col8.plotly_chart(fig_hist1, use_container_width=True)

    fig_hist2 = px.histogram(
        df,
        x="precip_mm",
        title="🌧 Precipitation Distribution",
        log_y=True
    )

    col9.plotly_chart(fig_hist2, use_container_width=True)

    st.info("📌 Insight: Precipitation is heavily skewed, indicating uneven rainfall distribution.")

# -----------------------------
# 🔗 CORRELATION
# -----------------------------
st.subheader("🔗 Correlation Between Climate Variables")

corr_data = filtered_df[[
    "temperature_celsius",
    "humidity",
    "wind_kph",
    "pressure_mb",
    "precip_mm"
]].corr()

fig_corr, ax = plt.subplots(figsize=(5, 3))

sns.heatmap(
    corr_data,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5,
    ax=ax
)

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.pyplot(fig_corr)

st.info("📌 Insight: Relationships between variables are complex and often non-linear.")

# -----------------------------
# DATA PREVIEW
# -----------------------------
st.subheader("📄 Data Preview")
st.dataframe(filtered_df.head(50))

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.caption("Developed as part of ClimateScope Project | Interactive Climate Analytics Dashboard")