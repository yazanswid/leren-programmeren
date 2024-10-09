# Maak een programma dat 2 gehele getallen opvraagt aan de gebruiker. Stel die getallen zijn toegekend aan de variabelen a en b
# Bepaal (met een if-statement) of a groter is dan b
# Zo ja:
# Ken de waarde van a toe aan een variabele Max
# Laat het programma printen: ‘a is het grootste getal: ’ gevolgd door de waarde van Max
# Doe een commit met de titel “input en if-statement”
# Breidt het programma uit.
def max_min(nr1: int, nr2: int) -> str:
    if nr1 == nr2:
        return (f"beide zijn gelijk")
    elif nr1>nr2:
        return (f"{nr1} is groter dan {nr2}")
    else:
        return (f"{nr2}is groter dan {nr1}")
    








resultaat = max_min(10, 20)
print(resultaat)