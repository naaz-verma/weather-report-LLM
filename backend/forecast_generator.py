from prophet import Prophet
import pandas as pd

def generate_forecast(csv_path='C:/Users/ASUS/Desktop/hackathon/weather-report-LLM/dataset/_hyd_Temps.csv', city="Hyderabad", periods=2555):  # 7 years × 365
    df = pd.read_csv(csv_path)
    df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
    df = df.dropna(subset=['Date'])
    df.rename(columns={"Date": "ds", "Temp Max": "y"}, inplace=True)

    model = Prophet(yearly_seasonality=True, daily_seasonality=False)
    model.fit(df[['ds', 'y']])

    future = model.make_future_dataframe(periods=periods)
    forecast = model.predict(future)

    forecast['City'] = city
    forecast['Month'] = forecast['ds'].dt.month
    forecast['Year'] = forecast['ds'].dt.year

    # Output only June–July of future years
    june_july = forecast[
        (forecast['Month'].isin([6, 7])) & (forecast['Year'] >= 2023)
    ][['ds', 'yhat', 'City', 'Month', 'Year']]

    return june_july
