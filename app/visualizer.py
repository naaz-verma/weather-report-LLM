import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import matplotlib.dates as mdates

from backend.analyze_forecast import load_weather_data, detect_anomalies, flag_heatwave_periods

def get_weather_df():
    df = load_weather_data()
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')  # Convert to datetime
    df = df.dropna(subset=['Date'])  # Remove invalid dates
    df = df.sort_values(by='Date')  # Ensure sorted
    df = detect_anomalies(df)
    df = flag_heatwave_periods(df)
    return df


def plot_heatwave_timeline():
    st.subheader("🔥 Heatwave Timeline")

    weather_df = get_weather_df()
    heatwave_df = weather_df[weather_df["heatwave"] == True]

    # Create figure and plot
    fig, ax = plt.subplots(figsize=(12, 5))

    # Line plot for Max Temperature
    sns.lineplot(data=weather_df, x="Date", y="Temp Max", label="Max Temperature", ax=ax, color="orange")

    # Highlight heatwave days with red scatter points
    sns.scatterplot(data=heatwave_df, x="Date", y="Temp Max", color="red", label="Heatwave Day", ax=ax, s=60)

    # Add moving average for temperature
    weather_df["7-day MA"] = weather_df["Temp Max"].rolling(window=7).mean()
    sns.lineplot(data=weather_df, x="Date", y="7-day MA", label="7-Day Moving Avg", ax=ax, color="brown", linestyle="--")

    # Axis formatting
    ax.set_title("📈 Heatwave Detection Over Time", fontsize=14)
    ax.set_ylabel("Temperature (°C)")
    ax.set_xlabel("Date")

    ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    ax.xaxis.set_major_locator(mdates.AutoDateLocator())
    ax.tick_params(axis='x', labelrotation=45)

    ax.legend(loc="upper left")
    ax.grid(True, linestyle="--", alpha=0.5)

    st.pyplot(fig)

    # Calculate Heatwave Stats
    total_heatwaves = heatwave_df.shape[0]
    longest_heatwave_period = (heatwave_df['Date'].max() - heatwave_df['Date'].min()).days
    max_temp_heatwave = heatwave_df['Temp Max'].max()

    # Display stats as a table
    stats_data = {
        "Total Heatwave Days": [total_heatwaves],
        "Longest Heatwave Period (days)": [longest_heatwave_period],
        "Max Temperature During Heatwave (°C)": [max_temp_heatwave]
    }
    stats_df = pd.DataFrame(stats_data)

    st.subheader("📊 Heatwave Statistics")
    st.table(stats_df)
