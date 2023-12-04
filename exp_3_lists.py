# %% lijst definieren
ages_list = [15, 29, 21, 13, 22, 50, 34]

# %% selecteren
ages_list[0]

# %% elementen toevoegen aan de list
print(ages_list)
ages_list.append(18)
print(ages_list)

# %% Sorteren: a. obv de method
ages_list.sort(reverse=False)
ages_list

# %%
sorted(ages_list, reverse=True)


# %%
ages_list_2 = [18, 25, 50, 33]

# %% subselectie/slice
ages_list_2[-4:-1]

# %%
ages_list_2[:-1]

# %% Unieke waarden in een list
list(set(ages_list))

# %%
min(ages_list_2)

#%%
max(ages_list_2)

# %%
sum(ages_list_2)

#%%

