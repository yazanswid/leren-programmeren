
fruit_lijst = ['appel', 'banaan', 'kers', 'druif', 'mango', 'peer']


print("Originele lijst van fruit:", fruit_lijst)


try:
    index = int(input("Voer een index in om het fruit te verwijderen (0 tot 5): "))

   
    if 0 <= index < len(fruit_lijst):
       
        verwijderde_vruit = fruit_lijst.pop(index)
        
       
        print("Verwijderd fruit:", verwijderde_vruit)
        
        
        print("Bijgewerkte lijst van fruit:", fruit_lijst)
    else:
        print("Ongeldige index. Voer een index in tussen 0 en", len(fruit_lijst) )

except ValueError:
    print("Voer aub een geldig geheel getal in.")
