#Maak een programma met een list met waarin 6 kleuren zitten (je vraagt ze dus niet aan de gebruiker).
kleuren_lijst = ['rood', 'blauwe', 'roos', 'rood', 'zwart', 'wit']
#Schrijf code die de gebruiker vraagt om hun naam en favoriete kleur. 
naam = input("wat is je naam?")
favoriete_kleur = input("wat je favoriete kleur?")
#Controleer of de favoriete kleur van de gebruiker in de list voorkomt.
if favoriete_kleur in kleuren_lijst:
    print(f"Hallo {naam}, wat een geweldige keuze!")
    print(f"De kleur {favoriete_kleur} is heel mooi!")

#In het geval dat de kleur voorkomt print je klein gedichtje/textje (gebruik hier voor chatgpt of verzin zelf) met daarin de naam van de gebruiker en gekozen kleur.
if favoriete_kleur in kleuren_lijst:
    print(f"Hallo {naam}, wat een geweldige keuze!")
    print(f"De kleur {favoriete_kleur} is net zo uniek als jij!")
else:
    print(f"Psst {naam}, deze kleur is niet zo geweldig! Als:")
    print((kleuren_lijst))
#Anders print je: "Psst {naamgebruiker}, deze kleur is niet zo geweldig! als: " en vervolgens de kleuren uit jouw lijst