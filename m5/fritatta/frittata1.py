from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
nr_persons = int(input("Voer het aantal personen in: ")) # replace this with better input

# ----- CALCULATIONS ----
# calculate factor 
factor = nr_persons / RECIPE_PERSONS
# calculate amount_eggs
amount_eggs = round(AMOUNT_EGGS * factor)
# calculate amount_milk
amount_milk = round(AMOUNT_MILK * factor)

# calculate amount_salt
amount_salt = round(AMOUNT_SALT * factor)

# calculate amount_pepper
amount_pepper = round(AMOUNT_PEPPER * factor)

# calculate amount_oil
amount_oil = round(AMOUNT_OIL * factor)

# calculate amount_onions
amount_onions = round(AMOUNT_ONIONS * factor)

# calculate amount_garlics
amount_garlics = round(AMOUNT_GARLICS * factor)

# calculate amount_spinach
amount_spinach = round(AMOUNT_SPINACH * factor)

# calculate amount_paprikas
amount_paprikas = round(AMOUNT_PAPRIKAS * factor)

# calculate amount_cheese
amount_cheese = round(AMOUNT_CHEESE * factor)

# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} personen:')
print('-----------------------------------------------')
# print (formatted) all amounts and units combined with their ingrediënt descriptions
print(f'{amount_eggs:2} x {UNIT_EGGS} {TXT_EGGS}')
print(f'{amount_milk:2} x {UNIT_MILK} {TXT_MILK}')
print(f'{amount_salt:2} x {UNIT_SALT} {TXT_SALT}')
print(f'{amount_pepper:2} x {UNIT_PEPPER} {TXT_PEPPER}')
print(f'{amount_oil:2} x {UNIT_OIL} {TXT_OIL}')
print(f'{amount_onions:2} x {UNIT_ONIONS} {TXT_ONIONS}')
print(f'{amount_garlics:2} x {UNIT_GARLICS} {TXT_GARLICS}')
print(f'{amount_spinach:2} x {UNIT_SPINACH} {TXT_SPINACH}')
print(f'{amount_paprikas:2} x {UNIT_PAPRIKAS} {TXT_PAPRIKAS}')
print(f'{amount_cheese:2} x {UNIT_CHEESE} {TXT_CHEESE}')
print('-----------------------------------------------')