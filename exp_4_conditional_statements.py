#%% 
import sys


#%%
age = 17
naam = "Dirk"
code = "ABC"

if age > 18:
    # wordt alleen uitgevoerd als statement True is
    print("Proost")
else naam == "Dirk":
    invoer_code = input("Geef de geheime code aan")
    if invoer_code == code:
        print("Dat is de goede code")
    else:
        print("Toch helaas")
else:
    print("Helaas")
    print("Tweede")
    #sys.exit()

    
print("We gaan door met de rest van de code")


# %%
gasten = []

# %%
gasten_lijst = ['Arie', 'Jaap', 'Dirk']
wachtwoord = "ABC"

age = 17
name = input("Voer je naam in:")
ingevoerd_wachtwoord = input("Voer wachtwoord in:")


if (name in gasten_lijst or ingevoerd_wachtwoord == wachtwoord) \
    and age > 18:
    if name not in gasten:
        print("Welkom")
        gasten.append(name)
    else:
        print("Je staat er al in")
else:
    print("❌ Helaas")


# %%


if "a" in "Arie".lower():
    print("Je naam bevat een A")



# %%
doel_bedrag = 1000

donaties = 400

aantal_donaties = 0
gedoneerd_bedrag = 0

while gedoneerd_bedrag < doel_bedrag:
    gedoneerd_bedrag += 400
    aantal_donaties += 1
    print(f"Gedoneerd bedrag: {gedoneerd_bedrag}")
    print(f"Aantal donaties: {aantal_donaties}")


# %%
