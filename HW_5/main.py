import requests
import pandas as pd

api_key = '2f5663123ef146d39bc103050252106'
url = "https://api.open-meteo.com/v1/forecast"
params = {
	"latitude": 50.4501,
	"longitude": 30.5236,
	"hourly": ["temperature_2m", "wind_speed_10m"],
	"timezone": "Europe/Moscow",
	"start_date": "2025-06-21",
	"end_date": "2025-06-28"
}
#такі params були написані прямо на самому сайті, дякую, дуже мило
response = requests.get(url, params=params)
data = response.json()
print(data)

df = pd.DataFrame(data['hourly'])

#df_three_days = df[(df['time'].dt.date >= pd.to_datetime('2025-06-21').date()) & (df['time'].dt.date <= pd.to_datetime('2025-06-23').date())]
#пробувала ще фільтрацією розібратись але це булшіт з інтернету, для цього без фільтру я знайшла спосіб лише head
df_three_days = df.head(72)
print(df_three_days)
#head(72) взяв мені перші 72 години щоб знайти макс мін та сер за наступні три дні (сподіваюсь завдання мало наувазі їх разом)
min_temp = df_three_days['temperature_2m'].min()
#temperature_2m з документації сайту https://open-meteo.com/en/docs
print(min_temp)
max_temp = df_three_days['temperature_2m'].max()
print(max_temp)
mean_temp = df_three_days['temperature_2m'].mean()
print(mean_temp)
#далі я робила не для трьох днів а для усіх
mean_wind = df['wind_speed_10m'].mean()
above_mean_wind = df[df['wind_speed_10m'] > mean_wind]
print(above_mean_wind)
cnt_above_mean_wind = above_mean_wind.shape[0]
print(cnt_above_mean_wind)