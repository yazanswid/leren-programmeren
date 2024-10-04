import random

# Selecteer 2 nummers
num1 = random.randint(1, 10)  
num2 = random.randint(5, 15)   

# Vraag om een antwoord
number = input(f'Weet jij wat {num1} + {num2} is? ') 

# Geef reactie op het antwoord
try:
    antwoord = int(number)  
    if antwoord == num1 + num2:  
        print('Dat is juist!')
    else:
        print('Nee, dat klopt niet.')  
except ValueError:   
    print('Dat is geen nummer!')  