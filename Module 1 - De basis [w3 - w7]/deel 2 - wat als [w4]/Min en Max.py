# Maak een programma dat 2 gehele getallen opvraagt aan de gebruiker. Stel die getallen zijn toegekend aan de variabelen a en b
# Bepaal (met een if-statement) of a groter is dan b
# Zo ja:
# Ken de waarde van a toe aan een variabele Max
# Laat het programma printen: ‘a is het grootste getal: ’ gevolgd door de waarde van Max
# Doe een commit met de titel “input en if-statement”
# Breidt het programma uit.

a = int(input("voer het eerste getal in"))
b = int(input("voer het tweede getal in "))
# Breidt het programma uit.
# Bepaal (met een elif-statement) of a kleiner is dan b
# Zo ja:
# Ken de waarde van a toe aan een variabele Min
# Laat het programma printen: ‘a is het kleinste getal: ’ gevolgd door de waarde van Min

min = a
max = b

if a > b :
    max = a
    min = b
    print(f"a is het grootste getal: {max} ")
    
    
elif b > a :
    max = b
    min = a
    print(f"b is het grootste getal: {max} ")
# Bepaal (met een else-statement) of a gelijk is aan b
# Zo ja:
# Laat het programma printen: ‘a en b zijn even groot’
# Doe een commit met de titel “else-statement”
# Breidt het programma uit.
else :
    
    Min = a  
    Max = a  
    print('a en b zijn even groot')



# Zorg dat in alle gevallen de variabelen Min en Max de juiste waarde krijgen
# Laat het programma daarna (dus in alle gevallen) printen:
# ‘Het minimum is: ’ gevolgd door de waarde van Min
# Het maximum is: ’ gevolgd door de waarde van Max

print(f'Het minimum is: {min}')
print(f'Het maximum is: {max}')