from recipe_lib import *
from frittata_ingredients import *

# -------- TITLE --------
print('=============== Frittata recept ===============')
# -------- INPUT --------
# use recipe_lib for input of nr_persons
# accepteer ook onhele (komma) personen
nr_persons = float(input("Voer het aantal personen in: "))

# ----- CALCULATIONS ----
# calculate factor
factor = nr_persons / RECIPE_PERSONS
# calculate amount_eggs
amount_eggs = round_piece(AMOUNT_EGGS * factor)
# calculate amount_milk
amount_milk = round_quarter(AMOUNT_MILK * factor)

# calculate amount_salt
amount_salt = round_quarter(AMOUNT_SALT * factor)

# calculate amount_pepper
amount_pepper = round_quarter(AMOUNT_PEPPER * factor)

# calculate amount_oil
amount_oil = round_quarter(AMOUNT_OIL * factor)

# calculate amount_onions 
amount_onions = round_piece(AMOUNT_ONIONS * factor)

# calculate amount_garlics
amount_garlics = round_piece(AMOUNT_GARLICS * factor)

# calculate amount_spinach
amount_spinach = round_quarter(AMOUNT_SPINACH * factor)

# calculate amount_paprikas
amount_paprikas = round_piece(AMOUNT_PAPRIKAS * factor)

# calculate amount_cheese
amount_cheese = round_quarter(AMOUNT_CHEESE * factor)

# -------- OUTPUT -------
print('=============== Frittata recept ===============')
print(f'Ingrediënten voor {nr_persons} {str_single_plural(nr_persons, "persoon")} personen:')
print('-----------------------------------------------')
# print (formatted) all amounts and units combined with their ingrediënt descriptions
print(f'{str_amount_fraction(amount_eggs)} {UNIT_EGGS} {str_single_plural(amount_eggs, TXT_EGGS)}')
print(f'{str_amount_fraction(amount_milk)} {str_units(amount_milk, UNIT_MILK)} {str_single_plural(amount_milk, TXT_MILK)}')
print(f'{str_amount_fraction(amount_salt)} {str_units(amount_salt, UNIT_SALT)} {str_single_plural(amount_salt, TXT_SALT)}')
print(f'{str_amount_fraction(amount_pepper)} {str_units(amount_pepper, UNIT_PEPPER)} {str_single_plural(amount_pepper, TXT_PEPPER)}')
print(f'{str_amount_fraction(amount_oil)} {str_units(amount_oil, UNIT_OIL)} {str_single_plural(amount_oil, TXT_OIL)}')
print(f'{str_amount_fraction(amount_onions)} {UNIT_ONIONS} {str_single_plural(amount_onions, TXT_ONIONS)}')
print(f'{str_amount_fraction(amount_garlics)} {UNIT_GARLICS} {str_single_plural(amount_garlics, TXT_GARLICS)}')
print(f'{str_amount_fraction(amount_paprikas)} {UNIT_PAPRIKAS} {str_single_plural(amount_paprikas, TXT_PAPRIKAS)}')
print(f'{str_amount_fraction(amount_spinach)} {UNIT_SPINACH} {str_single_plural(amount_spinach, TXT_SPINACH)}')
print(f'{str_amount_fraction(amount_cheese)} {str_units(amount_cheese, UNIT_CHEESE)} {str_single_plural(amount_cheese, TXT_CHEESE)}')
print('-----------------------------------------------')