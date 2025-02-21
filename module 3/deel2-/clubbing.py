PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

#bouw hieronder de floowchart na

PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

def leeftijd_toeganger():
    leeftijd = int(input("Hoe oud ben je? "))
    if leeftijd < 18:
        print("Sorry, je mag niet naar binnen.")
        print(f"Probeer het over {18 - leeftijd} jaar nog eens.")
        return 
    
    naam = input("Wat is je naam? ").strip().lower()
    vip = naam in VIP_LIST
    bandje = 'blauw' if leeftijd >= 21 else 'rood'
    
    if vip is False and  leeftijd >= 21:
        print("Je krijgt van mij een stempel.")
    else:
        print(f"Je krijgt van mij een {bandje} bandje.")
    
    while True:
        drankje = input(f"Wat wil je drinken? {DRANKJES}: ").strip().lower()
        
        if drankje not in DRANKJES:
            print("Sorry, geen idee wat je bedoelt, hier een glaasje water.")
            continue
        
        if drankje == "cola":
            print("Alsjeblieft, complimenten van het huis.")
        elif drankje == "bier":
            if leeftijd >= 21 or bandje == "blauw":
                print(f"Alsjeblieft je {drankje}, dat is dan €{PRIJS_BIER}")
            else:
                print("Sorry, je mag geen alcohol bestellen onder de 21.")
                print(f"Probeer het over {21 - leeftijd} jaar nog eens.")
        elif drankje == "champagne":
            if vip:
                print(f"Alsjeblieft je {drankje}, dat is dan €{PRIJS_CHAMPAGNE}")
            else:
                print("Sorry, alleen VIPs mogen champagne bestellen.")
                
        
        print("Einde programma.")

leeftijd_toeganger()



        








    

  



        
    

