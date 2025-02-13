from fruitmand import fruitmand

round_fruits = [fruit['name'] for fruit in fruitmand if fruit['round']]
print("Ronde fruitsoorten:")
print((round_fruits))
