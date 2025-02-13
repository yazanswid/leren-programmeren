from fruitmand import fruitmand



gesorteerde_fruitmand = sorted(fruitmand, key = lambda x: x['weight'])







for fruit in reversed(gesorteerde_fruitmand):
    gewicht_in_kg = fruit['weight'] / 1000
    print(fruit['name'] + " - " + str(gewicht_in_kg) + " kg")

