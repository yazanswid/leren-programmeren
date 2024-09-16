#Schrijf een eenvoudig Python-programma dat bepaalt of een persoon toegang heeft tot een evenement. De persoon mag alleen toegang krijgen als hij/zij ouder is dan 18 jaar.
leeftijd = int(input("Voer je leeftijd in: "))
#Stappen:

#1. Vraag de gebruiker om zijn/haar leeftijd in te voeren.
geen_toegang = not (leeftijd > 18)
if geen_toegang:
 print("Je hebt geen toegang tot het evenement.")
else:
    print("Je hebt toegang tot het evenement.")