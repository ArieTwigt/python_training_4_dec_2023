#%%
import requests
import pandas


#%% specify the car brand
selected_plate = input("Insert the car license plate:\n").upper()

#%% endpoint
endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?kenteken={selected_plate}"

#%% execute the request
response =  requests.get(endpoint)

# %% check the response status
response.status_code

# %% get the data from the response
data = response.json()

# %% create a pandas DataFrame from the data
data_df = pandas.DataFrame(data)

# %% show the DataFrame
data_df
# %% Export the data
print("Exporting")

data_df.to_csv(f"{selected_plate}_export.csv",
               sep=";",
               index=False)

print("✅ Succesfully exported")