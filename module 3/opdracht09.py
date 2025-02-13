from fruitmand import fruitmand

fruitmand = [fruit for fruit in fruitmand if fruit['name'] != 'druif']
kleuren = {}
for fruit in fruitmand:
    kleuren.setdefault(fruit['color'], fruit['name'])
print("\n".join(kleuren.values()))
