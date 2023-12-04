# %% F-strings
naam = "Arie"

#%% Met +
print("Hello " + " " + naam)

# %%
print(f"Hello {naam}")

# %% De "upper()" method
naam.upper()

# %% De "replace()" method
naam.replace("i", "o")

# %% split: str -> list
naam.split("i")
# %%
verhaal = """
Dit is een heel lang verhaal

"""
# %%
verhaal_list = verhaal.split(" ")
# %% join: list -> str
" ".join(verhaal_list)

# %%
