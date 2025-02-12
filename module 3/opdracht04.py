from fruitmand import fruitmand

import random

aantal = int(input("Hoeveel fruitnamen wil je zien? "))

for _ in range(aantal):
    random_fruit = random.choice(fruitmand)
    print(random_fruit['name'])
