
print("Je hebt het maximale aantal pogingen bereikt. Je mag niet meer inloggen.")


print("\nNieuw programma: Optellen van getallen vanaf 50")

som = 0
getal = 50

while som <= 1000:
    som += getal
    print(f"Huidig getal: {getal}, Som: {som}")
    getal += 1

print(f"De som is groter dan 1000. Het laatste getal dat werd opgeteld was {getal - 1}.")
print(f"De uiteindelijke som is {som}.")