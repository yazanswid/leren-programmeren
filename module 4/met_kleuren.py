# output_met_kleuren.py

from termcolor import colored
from naam__en_leeftijd import *

alle_gegevens = verzamel_gegevens()

for persoon in alle_gegevens:
    naam = colored(persoon['naam'], 'green')
    woonplaats = colored(persoon['woonplaats'], 'yellow')
    leeftijd = int(persoon['leeftijd'])
    if leeftijd >= 18:
        leeftijd_tekst = colored(f"al {leeftijd} jaar", 'red')
        volwassen = "volwassen"
    else:
        leeftijd_tekst = colored("nog niet", 'red')
        volwassen = "volwassen"
    
    print(f"In {woonplaats} woont {naam}, die {leeftijd_tekst} {volwassen} is.")
