#%% 
import requests
import os
import pandas

from dotenv import load_dotenv

load_dotenv()

# Voor een key, zelf even een key aanmaken op OpenWeatherMap
OPENWEATHERMAPKEY = os.environ.get('OPENWEATHERMAPKEY')

#%% ask for the city
print("☁️ Welcome to the weather predictor\n")
city = input("Select the city:\n")

#%% endpoint
endpoint = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&units=metric&appid={OPENWEATHERMAPKEY}"

# %%
response = requests.get(endpoint)

#%%
data = response.json()

#%% convert to a DataFrame
data_list = data['list']


# %% prepare the empty lists that will collect the data
weather_dates = []
temperatures = []
temp_mins = []
temp_maxs = []
feels_likes = []
rain_mms = []
descriptions = []
wind_speeds = []


#%% Iterate over all the values in "list" (these are 40 predictions)
for prediction in data_list:
    weather_dates.append(prediction['dt_txt'])
    temperatures.append(prediction['main']['temp'])
    temp_mins.append(prediction['main']['temp_min'])
    temp_maxs.append(prediction['main']['temp_max'])
    feels_likes.append(prediction['main']['feels_like'])
    if 'rain' in prediction.keys(): # rain is only in the keys if it rains
        rain_mms.append(prediction['rain']['3h'])
    else:
        rain_mms.append(0)
    descriptions.append(prediction['weather'][0]['description'])
    wind_speeds.append(prediction['wind']['speed'])


# %% Create a Pandas DataFrame
data_df = pandas.DataFrame({
    "date": weather_dates,
    "description": descriptions, 
    "temperature": temperatures,
    "wind_speed": wind_speeds,
    "rain_mm": rain_mms,
    "min_temperature": temp_mins,
    "max_temperature": temp_maxs,
    "feel_temperature": feels_likes,
})

### Pandas

#%% visualize
data_df.plot.bar(x="date", 
                 y=["temperature", "rain_mm", "wind_speed"], 
                 subplots=True,
                 title=f"Weather prediction for {city}")



# %%
data_df.to_csv(f"data/weather/weersvoorspellingen_{city}.csv", sep=";", index=False)

# %%
print("Exported weather to csv\n\n")
print(data_df)