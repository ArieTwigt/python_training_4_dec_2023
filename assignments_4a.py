#%%
from datetime import date

#%% define the date of today
today_date = date.today()

# %% define my birthday
my_next_birthday = date(2024, 4, 1)

# %% subtract the two days
days_to_birthday = my_next_birthday - today_date
# %% show the difference
days_to_birthday

#%% Get the value from the timedelta
days_to_birthday.days
# %%
