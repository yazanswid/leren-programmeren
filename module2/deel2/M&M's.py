import random



kleuren = ("oranje", "blauw", "groen", "bruin")


def vul_zak(aantal):
    zak = []
    for _ in range(aantal):
        zak.append(random.choice(kleuren))
    return zak

aantal_mms = int(input("Hoeveel M&M's wil je aan de zak toevoegen? "))


mm_zak = vul_zak(aantal_mms)


print("De inhoud van de zak met M&M's is:")
print(mm_zak)