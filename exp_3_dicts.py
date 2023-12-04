#%%
person_dict = dict()

#%%
person_dict = {}

# %%
person_dict['name'] = "James"
person_dict

# %%
person_dict['age'] = 40
person_dict

# %%
person_dict_2 = {"name": "Mary", 
                 "age": 40}

# %%
family_dict = {}
family_dict['name'] = "Jones"
family_dict['members'] = []

# %%
print(person_dict)
print(person_dict_2)

#%%
family_dict
# %%
family_dict['members'].append(person_dict)
# %%
family_dict
# %%
family_dict['members'].append(person_dict_2)
# %%
family_dict.keys()
# %%
family_dict.values()
# %%
family_dict['members'][1]['age']
# %%
