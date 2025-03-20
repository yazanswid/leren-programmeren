
dagen = ("maandag", "dinsdag", "woensdag", "donderdag", "vrijdag", "zaterdag", "zondag")


print("Alle dagen van de week zijn:", ", ".join(dagen))


print("De weekenddagen zijn:", ", ".join(dagen[-2:]))


print("De werkdagen zijn:", ", ".join(dagen[:5]))


print("Alle dagen van de week in omgekeerde volgorde zijn:", ", ".join(reversed(dagen)))


print("De werkdagen in omgekeerde volgorde zijn:", ", ".join(reversed(dagen[:5])))


print("De weekenddagen in omgekeerde volgorde zijn:", ", ".join(reversed(dagen[-2:])))
