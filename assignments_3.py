### Assignment 1


#%% a
person_1 = {} # initate an empty dict
person_1['name'] = "Jim"
person_1['age'] = 30
person_1['hobbies'] = ['cycling', 'football', 'reading']

print(person_1)

# %% b
person_1 = {"name": "Jim",
            "age": 30,
            "hobbies":  ['cycling', 'football', 'reading']
            }

### Assignment 2


# %%
person_2 = {} # initate an empty dict
person_2['name'] = "Mary"
person_2['age'] = 30
person_2['hobbies'] = ['tennis', 'boxing', 'running']

person_3 = {} # initate an empty dict
person_3['name'] = "Bobby"
person_3['age'] = 12
person_3['hobbies'] = ['gaming', 'skateboard']

person_4 = {} # initate an empty dict
person_4['name'] = "Ann"
person_4['age'] = 15
person_4['hobbies'] = ['cooking', 'baseball']

# %% a. create a dictionary that contains the family

family = [person_1, person_2, person_3, person_4]

print(family)

# %% b.
family_dict = {}
family_dict['name'] = 'Jones'
family_dict['members'] = [person_1, person_2, person_3, person_4]


# %%
family_dict['members'][2]['age']

# %%
