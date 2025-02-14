from fruitmand import fruitmand

kleuren = {fruit['color']for fruit in fruitmand}

while True:
    gekozen_kleuren = input(f'kies een kleur van de beschikbareb kleuren {kleuren}')
    if gekozen_kleuren in kleuren:
        print(f'Je hebt gekozen kleur {gekozen_kleuren}')
        break
    print(f'kluer zit er niet bij')

ronde_fruiten = sum(1 for fruit in fruitmand if fruit['color'] == gekozen_kleuren and fruit['round'])
niet_ronde_fruiten = sum( 1 for fruit in fruitmand if fruit['color'] == gekozen_kleuren and not fruit['round'])


if ronde_fruiten > niet_ronde_fruiten:
    print(f"Er zijn {ronde_fruiten - niet_ronde_fruiten} meer ronde vruchten dan niet ronde vruchten in de kleur {gekozen_kleuren}")

elif ronde_fruiten < niet_ronde_fruiten:
    print(f"Er zijn {ronde_fruiten - niet_ronde_fruiten} minder ronde vruchten dan niet ronde vruchten in de kleur {gekozen_kleuren}")
else:
    print(f"Er zijn {ronde_fruiten} ronde vruchten en {niet_ronde_fruiten} niet ronde vruchten in de kleur {gekozen_kleuren}")