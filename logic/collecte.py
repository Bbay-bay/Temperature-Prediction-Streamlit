import openmeteo_requests
import requests_cache
import pandas as pd
from retry_requests import retry

cache_session = requests_cache.CachedSession('.cache', expire_after = -1)
retry_session = retry(cache_session, retries = 5, backoff_factor = 0.2)
openmeteo = openmeteo_requests.Client(session = retry_session)

url = "https://archive-api.open-meteo.com/v1/archive"

def collecter(lat,long):
    params = {
	"latitude": lat,
	"longitude": long,
	"start_date": "2014-12-01",
	"end_date": "2024-12-01",
	"hourly": "relative_humidity_2m",
	"daily": ["weather_code", "temperature_2m_mean", "precipitation_sum"]
    }
    responses = openmeteo.weather_api(url, params=params)
    response = responses[0]

    #humidite par heure

    hourly = response.Hourly()
    hourly_relative_humidity_2m = hourly.Variables(0).ValuesAsNumpy()

    hourly_data = {"date": pd.date_range(
        start = pd.to_datetime(hourly.Time(), unit = "s", utc = True),
        end = pd.to_datetime(hourly.TimeEnd(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = hourly.Interval()),
        inclusive = "left"
    )}
    hourly_data["relative_humidity_2m"] = hourly_relative_humidity_2m
    hourly_dataframe = pd.DataFrame(data = hourly_data)
    hourly_dataframe["date"] = hourly_dataframe["date"].dt.date

    #Transformation de l'humidite par heure a l'humidite par jour:

    daily_humidity = hourly_dataframe.groupby("date")["relative_humidity_2m"].agg(
    mean="mean"
    ).reset_index()
    daily = response.Daily()
    daily_weather_code = daily.Variables(0).ValuesAsNumpy()
    daily_temperature_2m_mean = daily.Variables(1).ValuesAsNumpy()
    daily_precipitation_sum = daily.Variables(2).ValuesAsNumpy()

    daily_data = {"date": pd.date_range(
        start = pd.to_datetime(daily.Time(), unit = "s", utc = True),
        end = pd.to_datetime(daily.TimeEnd(), unit = "s", utc = True),
        freq = pd.Timedelta(seconds = daily.Interval()),
        inclusive = "left"
    )}
    daily_data["weather_code"] = daily_weather_code
    daily_data["temperature_2m_mean"] = daily_temperature_2m_mean
    daily_data["precipitation_sum"] = daily_precipitation_sum
    daily_dataframe = pd.DataFrame(data = daily_data)
    daily_dataframe["date"] = daily_dataframe["date"].dt.date

    #On emerge les deux dataframe :
    meteo_10ans = pd.merge(
        daily_dataframe,
        daily_humidity,
        how="left",
        on="date"
    )

    meteo_10ans = meteo_10ans.drop(columns=["weather_code"])
    meteo_10ans.rename(columns={
    "date": "Date",
    "temperature_2m_mean": "Temperature moyenne (°C)",
    "precipitation_sum": "Precipitation (mm)",
    "mean": "Humidite moyenne (%)",
    }, inplace=True)

    return meteo_10ans

'''def get_stats(data: pd.DataFrame):
    mean=[]
    s=data.describe().to_dict()
    for key in s.keys():
        mean.append(s[key]["mean"])
    return mean'''
def get_stats(data: pd.DataFrame):
    return data.describe()