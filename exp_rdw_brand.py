#%%
import requests
import pandas


#%% specify the car brand
selected_brand = input("Insert the car brand:\n").upper()

#%% endpoint
endpoint = f"https://opendata.rdw.nl/resource/m9d7-ebf2.json?merk={selected_brand}"

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

data_df.to_csv(f"{selected_brand}_export.csv",
               sep=";",
               index=False)

# Print the car in the console
print(data_df)

print("✅ Succesfully exported")