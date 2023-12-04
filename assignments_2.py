# %%
first_name = "Erling"
last_name  = "Haaland"

full_name  = first_name + last_name
print(full_name)

#  the format function
full_name = "{} {}".format(first_name, last_name)
print(full_name)

# %%
full_name
# %%


### ASSIGNMENT 1:

#%% a. With +
full_name + " .Jr"

# %% b.
full_name_new = f"{full_name} .Jr"

### ASSIGNMENT 2:

#%%
full_name_new
# %% a
full_name_new.replace("Erling", "E.")

# %% b.
full_name_split = full_name_new.split(" ")
first_letter = full_name_split[0][0]
full_name_abbrv = f"{first_letter}. {full_name_split[1]} {full_name_split[2]}"
full_name_abbrv

# %%
