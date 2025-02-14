from fruitmand import fruitmand

fruitmand = [fruit for fruit in fruitmand if fruit['name'] != 'druif']
kleuren = []
for fruit in fruitmand:
    if not (fruit['color'] in kleuren):
        kleuren.append(fruit['color'])
        
print((kleuren))
