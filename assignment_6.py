### ASSIGNMENT 1

#%%
names_list = ['Jim', 'John', 'Marc', 'Danny', 'Peter']

names_list_new = []

vowels = "aeouiy"

#%%
for name in names_list:
    for letter in vowels:
        if letter in name:
            name = name.replace(letter, "")

    names_list_new.append(name)

# %%
names_list_new
# %%


### ASSIGNMENT 2

#%%
import datetime
import locale

locale.setlocale(locale.LC_ALL, 'nl_NL') 

#%%
today_date = datetime.date.today()


# %%
num_days = 10

for x in range(1, num_days + 1):
    new_date = today_date + datetime.timedelta(days=x)
    
    # get the name of the day name in the date
    day_name = new_date.strftime("%A, %B")
    print(day_name)



# %% b.

today_date = datetime.date.today()

num_days = 1
max_days = 10

while num_days <= 10:
    new_date = today_date + datetime.timedelta(days=num_days)

    # get the name of the day name in the date
    day_name = new_date.strftime("%A, %B")
    print(day_name)

    # 
    num_days += 1

# %%
