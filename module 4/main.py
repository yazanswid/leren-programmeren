from naam__en_leeftijd import *


alle_gegevens = verzamel_gegevens()
for persoon in alle_gegevens:
    print(f"{persoon['naam']}, die in {persoon['woonplaats']} woont, is  {persoon['leeftijd']} jaar")