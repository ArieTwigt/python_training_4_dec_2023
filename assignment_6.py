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
