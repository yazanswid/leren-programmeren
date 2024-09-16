getallen = [1, 2, 3, 4, 5, 6]


print("Voer 6 getallen in:")

for i in range(6):
    getal = float(input(f"Getal {i+1}: "))
    getallen.append(getal)


getallen.sort()


print("Gesorteerde lijst van laag naar hoog:")
print(getallen)