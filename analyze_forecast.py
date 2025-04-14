# analyze_forecast.py
import pandas as pd
import datetime
import re
from dateutil import parser

def load_weather_data(csv_path='C:/Users/ASUS/Desktop/hackathon/weather-report-LLM/dataset/_hyd_Temps.csv'):
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
    df = df.dropna(subset=['Date'])
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

def extract_date_from_url(url: str):
    if not url:
        return None, None
    # Try finding YYYY-MM or YYYY/MM in the URL
    match = re.search(r'(\d{4})[/-](\d{1,2})', url)
    if match:
        return int(match.group(1)), int(match.group(2))
    # Try finding just year (4-digit) in URL
    match = re.search(r'(\d{4})', url)
    if match:
        return int(match.group(1)), None
    return None, None

def extract_date_from_text(text: str):
    try:
        words = text.split()
        for i in range(len(words) - 1):
            phrase = f"{words[i]} {words[i + 1]}"
            try:
                date = parser.parse(phrase, fuzzy=True, default=datetime.datetime(2000, 1, 1))
                return date.year, date.month
            except:
                continue
    except:
        return None, None
    return None, None

def check_consistency(text: str, url: str, df):
    year, month = extract_date_from_url(url)
    if not year:
        year, month = extract_date_from_text(text)

    if not year:
        return {"match": False, "reason": "No date found in news content or URL"}

    filtered = df[df['Year'] == year]
    if month:
        filtered = filtered[filtered['Month'] == month]

    if len(filtered) == 0:
        return {"match": False, "reason": f"No data available for {month or 'unknown month'}/{year}"}

    heatwave_days = filtered['heatwave'].sum()
    rain_days = filtered['heavy_Rain'].sum()

    if heatwave_days > 3:
        return {"match": True, "reason": f"Heatwave detected in {month or 'some month'}/{year} ({heatwave_days} days)"}
    elif rain_days > 2:
        return {"match": True, "reason": f"Heavy Rain detected in {month or 'some month'}/{year} ({rain_days} days)"}
    else:
        return {
            "match": False,
            "reason": f"No significant weather anomaly found in {month or 'some month'}/{year}",
            "heatwave_days": int(heatwave_days),
            "rain_days": int(rain_days)
        }

def analyze_forecast(text: str, url: str = ""):
    df = load_weather_data()
    df = detect_anomalies(df)
    df = flag_heatwave_periods(df)
    return check_consistency(text, url, df)
