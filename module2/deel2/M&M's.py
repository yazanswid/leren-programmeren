import random

kleuren = ("oranje", "blauw", "groen", "bruin")

def vul_zak(aantal):
    zak = [random.choice(kleuren) for _ in range(aantal)]
    kleur_aantallen = {kleur: zak.count(kleur) for kleur in kleuren}
    return kleur_aantallen

aantal_mms = int(input("Hoeveel M&M's wil je aan de zak toevoegen? "))

mm_zak = vul_zak(aantal_mms)

print("De inhoud van de zak met M&M's is:")
for kleur, aantal in mm_zak.items():
    print(f"{kleur}: {aantal}")