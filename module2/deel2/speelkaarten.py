import random

kleuren = ['harten','klavers','schopper','ruiten']
waarden = ['2' , '3' , '4' , '5' , '6','7','8','9', '10', 'boer','vrouw','heer', 'A']
deck = [f'{kleur} {waarde}' for kleur in kleuren for waarde in waarden] + ['joker','joker' ]

random.shuffle(deck)
getrokken_kaarten = deck[:7]
overgebleven_deck = deck[:7]


print("getrokken kaarten: ", ','.join(getrokken_kaarten))
print(f'\nAntal kaarten over in het deck: {len(overgebleven_deck)}')
print("Overgebleven kaarten in het deck:", ", ".join(overgebleven_deck))