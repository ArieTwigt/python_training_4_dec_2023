### ASSIGNMENT 1 

# %% a. 
name = "Dirk"

first_letter = name[0]

if first_letter.lower() == "a":
    print("Your name starts with an 'A'")
else:
    print("Your name does not start with an 'A'")



# %% b. -> Gebruikt de 'startswith' method
name = "Dirk"

if name.lower().startswith("a"):
    print("Your name starts with an 'A'")
else:
    print("Your name does not start with an 'A'")



### ASSIGNMENT 2

# %%
# definieer de klinkers
name = input("Enter your name:")

# handmatig definieeren van de klinkers
vowels = "aeoui"

# pak de eerste letter van de naam, en lowercase deze
first_letter = name[0]

# condtional statement
if first_letter.lower() in vowels:
    new_name = name.replace(first_letter, "R")
else:
    new_name = name.replace(first_letter, "A")

print(new_name)


### ASSIGNMENT 3

# %%
age = 17


if age >= 18 and age <= 68:
    print("You have to work")


# %%
age = 69
if 18 <= age <= 68:
    print("You have to work") 

    