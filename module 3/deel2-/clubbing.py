PRIJS_COLA = 1.80
PRIJS_BIER = 2.40
PRIJS_CHAMPAGNE = 12.30

DRANKJES = ('cola', 'bier', 'champagne')
VIP_LIST = ('jeroen', 'jouke', 'rudi')

def toegang_eisen():
    leeftijd = int(input("Hoe oud ben je? "))
    bandje = None  
    
    if leeftijd < 18:
        print("Sorry, je mag niet naar binnen.")
        print(f"Probeer het over {18 - leeftijd} jaar nog eens.")
        return 
    
    naam = input("Wat is je naam? ").strip().lower()
    vip = naam in VIP_LIST
    

    if leeftijd >= 21:
        if vip:
            bandje = "blauw"
            print(f"Je krijgt van mij een {bandje} bandje.")
        else:
            print("Je krijgt van mij een stempel.")
    elif vip:
        bandje = "rood"  
        print(f"Je krijgt van mij een {bandje} bandje.")
    else:
        print("Je mag naar binnen, maar geen alcohol bestellen.")

    while True:
        drankje = input(f"Wat wil je drinken? {DRANKJES}: ").strip().lower()

        if drankje not in DRANKJES:
            print("Sorry, geen idee wat je bedoelt, hier een glaasje water.")
            continue  

        if drankje == "cola":
            if bandje in ("rood", "blauw"):  
                print("Alsjeblieft, complimenten van het huis.")
            else:
                print(f"Alsjeblieft je {drankje}, dat is dan €{PRIJS_COLA:.2f}")

        elif drankje == "bier":
            if leeftijd >= 21 or bandje == "blauw": 
                print(f"Alsjeblieft je {drankje}, dat is dan €{PRIJS_BIER:.2f}")
            else:
                print("Sorry, je mag geen alcohol bestellen onder de 21.")
                print(f"Probeer het over {21 - leeftijd} jaar nog eens.")

        elif drankje == "champagne":
            if vip:  
                print(f"Alsjeblieft je {drankje}, dat is dan €{PRIJS_CHAMPAGNE:.2f}")
            else:
                print("Sorry, alleen VIPs mogen champagne bestellen.")

        print("Einde programma.")
        break

toegang_eisen()








    

  



        
    

