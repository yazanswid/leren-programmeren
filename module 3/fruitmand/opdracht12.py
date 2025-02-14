from fruitmand import fruitmand

def get_fruit_naam(get_fruit_naam):
    return max(get_fruit_naam, key=lambda fruit: len(fruit['name']))

langeste_fruit_naam = get_fruit_naam(fruitmand)
print(f"Kleur: {langeste_fruit_naam['color']}")
print(f"Gewicht: {langeste_fruit_naam['weight']} gram")
print(f"Naam: {langeste_fruit_naam['name']}")
print(f'{len(langeste_fruit_naam["name"])} letters')