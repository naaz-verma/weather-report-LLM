import pandas as pd
import datetime
from dateutil import parser

def load_weather_data(csv_path='C:/Users/ASUS/Desktop/hackathon/weather-report-LLM/dataset/_hyd_Temps.csv'):
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')  # handle DD-MM-YYYY
    df = df.dropna(subset=['Date'])  # remove any rows where date is invalid
    df['Year'] = df['Date'].dt.year
    df['Month'] = df['Date'].dt.month
    return df


def detect_anomalies(df):
    avg_Temp = df['Temp Max'].mean()
    df['Temp_anomaly'] = df['Temp Max'] > (avg_Temp + 4)
    df['heavy_Rain'] = df['Rain'] > 50
    return df

def flag_heatwave_periods(df):
    df['heatwave'] = False
    counter = 0
    for i in range(len(df)):
        if df.iloc[i]['Temp_anomaly']:
            counter += 1
        else:
            counter = 0
        if counter >= 3:
            df.iloc[i - 2:i + 1, df.columns.get_loc('heatwave')] = True
    return df

def check_consistency(summary_text, df):
    try:
        words = summary_text.split()
        for i in range(len(words) - 1):
            phrase = f"{words[i]} {words[i+1]}"
            try:
                date = parser.parse(phrase, fuzzy=True, default=datetime.datetime(2000, 1, 1))
                year, month = date.year, date.month
                break
            except:
                continue
        else:
            return {"match": False, "reason": "No date found in news"}
    except:
        return {"match": False, "reason": "Date parsing failed"}

    filtered = df[(df['Year'] == year) & (df['Month'] == month)]
    if len(filtered) == 0:
        return {"match": False, "reason": f"No data available for {month}/{year}"}

    heatwave_days = filtered['heatwave'].sum()
    rain_days = filtered['heavy_Rain'].sum()

    if heatwave_days > 3:
        return {"match": True, "reason": f"Heatwave detected in {month}/{year} ({heatwave_days} days)"}
    elif rain_days > 2:
        return {"match": True, "reason": f"Heavy Rain detected in {month}/{year} ({rain_days} days)"}
    else:
        return {
            "match": False,
            "reason": f"No significant weather anomaly found in {month}/{year}",
            "heatwave_days": int(heatwave_days),
            "rain_days": int(rain_days)
        }

def analyze_forecast(summary_text):
    df = load_weather_data()
    df = detect_anomalies(df)
    df = flag_heatwave_periods(df)
    return check_consistency(summary_text, df)
