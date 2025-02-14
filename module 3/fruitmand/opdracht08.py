from fruitmand import fruitmand

totaal_gewicht = sum(fruit['weight'] for fruit in fruitmand)
print(f"Totaal gewicht van de fruitmand: {totaal_gewicht} g")

watermeloen = {
    'name': 'watermeloen',
    'weight': 2500,
    'color': 'green',
    'round': True
}
fruitmand.append(watermeloen)


nieuw_totaal_gewicht = sum(fruit['weight'] for fruit in fruitmand)
print(f"Nieuw totaal gewicht van de fruitmand: {nieuw_totaal_gewicht} g")