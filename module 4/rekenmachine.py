# rekenmachine.py

from numpy import append

from funcies import addition, subtraction, multiplication, division

def vraag_getal(tekst):
    while True:
        try:
            return float(input(tekst))
        except ValueError:
            print("Ongeldige invoer. Voer een geldig getal in.")

first_round = True
uitkomst = False

while True:
    if first_round:
        print("Wat wil je doen?")
    else:
        print(f"\nWil je wat met de uitkomst ({uitkomst}) doen?")
    
    print("A) optellen")
    print("B) aftrekken")
    print("C) vermenigvuldigen")
    print("D) delen")
    print("E) ophogen")
    print("F) verlagen")
    print("G) verdubbelen")
    print("H) halveren")
    print("I) niets")

    keuze = input("Maak een keuze (A t/m I): ").strip().upper()

    if keuze == "I":
        if not first_round:
            print("Rekenmachine gestopt.")
            break
        else:
            print("Je moet eerst een berekening doen.")
            continue

    # Keuze omzetten naar actiea
    n1 = uitkomst if not first_round else False
    n2 = False

    if keuze in ['A', 'B', 'C', 'D']:  # 2 getallen nodig
        if n1 is False:
            n1 = vraag_getal("Voer het eerste getal in: ")
        n2 = vraag_getal("Voer het tweede getal in: ")
    elif keuze in ['E', 'F']:  # Ophogen of verlagen
        if n1 is False:
            n1 = vraag_getal("Voer een getal in: ")
        n2 = 1
    elif keuze in ['G', 'H']:  # Verdubbelen of halveren
        if n1 is False:
            n1 = vraag_getal("Voer een getal in: ")
        n2 = 2
    else:
        print("Ongeldige keuze. Probeer opnieuw.")
        continue

    # Uitvoering
    if keuze == "A":
        uitkomst = addition(n1, n2)
        print(f"{n1} + {n2} = {uitkomst}")
    elif keuze == "B":
        uitkomst = subtraction(n1, n2)
        print(f"{n1} - {n2} = {uitkomst}")
    elif keuze == "C":
        uitkomst = multiplication(n1, n2)
        print(f"{n1} x {n2} = {uitkomst}")
    elif keuze == "D":
        uitkomst = division(n1, n2)
        print(f"{n1} : {n2} = {uitkomst}")
    elif keuze == "E":
        uitkomst = addition(n1, n2)
        print(f"{n1} + 1 = {uitkomst}")
    elif keuze == "F":
        uitkomst = subtraction(n1, n2)
        print(f"{n1} - 1 = {uitkomst}")
    elif keuze == "G":
        uitkomst = multiplication(n1, n2)
        print(f"{n1} x 2 = {uitkomst}")
    elif keuze == "H":
        uitkomst = division(n1, n2)
        print(f"{n1} : 2 = {uitkomst}")

    first_round = False

