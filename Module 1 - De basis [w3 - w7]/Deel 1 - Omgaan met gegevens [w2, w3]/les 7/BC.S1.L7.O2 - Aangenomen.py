#Schrijf een programma met 3 variabelen:
#leeftijd = 18, snor = j (of n) en diploma = j (of n).
leeftijd = 18
snor = 'n'
diploma = 'n'

#Je schrijft een programma wat bepaalt of iemand is aangenomen. 
#Je bent aangenomen als je: 18 bent (of ouder) en een snor hebt of onder de 18 met een diploma.
if (leeftijd >= 18 and snor == 'j') and (leeftijd >= 18 and diploma == 'n'):
    print("gefeliseteerd, je bent aangenomen")
#Let op:
#Je mag maar 1 if statement gebruiken!!!
else: 
     print("Helaas, je bent niet aangenomen")
#Test je programma door de variabelen te wijzigen.