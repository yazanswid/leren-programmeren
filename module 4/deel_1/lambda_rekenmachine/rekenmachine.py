# rekenmachine.py

# Lambdas voor alle rekenkundige bewerkingen
operations = {
    'A': lambda x, y: x + y,
    'B': lambda x, y: x - y,
    'C': lambda x, y: x * y,
    'D': lambda x, y: "Kan niet delen door 0" if y == 0 else x / y,
    'E': lambda x, y: x + 1,
    'F': lambda x, y: x - 1,
    'G': lambda x, y: x * 2,
    'H': lambda x, y: x / 2,
}


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

    n1 = uitkomst if not first_round else False
    n2 = False

    if keuze in ['A', 'B', 'C', 'D']:
        if n1 is False:
            n1 = vraag_getal("Voer het eerste getal in: ")
        n2 = vraag_getal("Voer het tweede getal in: ")
    elif keuze in ['E', 'F']:
        if n1 is False:
            n1 = vraag_getal("Voer een getal in: ")
        n2 = 1
    elif keuze in ['G', 'H']:
        if n1 is False:
            n1 = vraag_getal("Voer een getal in: ")
        n2 = 2
    else:
        print("Ongeldige keuze. Probeer opnieuw.")
        continue

    if keuze == "A":
        uitkomst = operations[keuze](n1, n2)
        print(f"{n1} + {n2} = {uitkomst}")
    elif keuze == "B":
        uitkomst = operations[keuze](n1, n2)
        print(f"{n1} - {n2} = {uitkomst}")
    elif keuze == "C":
        uitkomst = operations[keuze](n1, n2)
        print(f"{n1} x {n2} = {uitkomst}")
    elif keuze == "D":
        uitkomst = operations[keuze](n1, n2)
        print(f"{n1} : {n2} = {uitkomst}")
    elif keuze == "E":
        uitkomst = operations[keuze](n1, n2)
        print(f"{n1} + 1 = {uitkomst}")
    elif keuze == "F":
        uitkomst = operations[keuze](n1, n2)
        print(f"{n1} - 1 = {uitkomst}")
    elif keuze == "G":
        uitkomst = operations[keuze](n1, n2)
        print(f"{n1} x 2 = {uitkomst}")
    elif keuze == "H":
        uitkomst = operations[keuze](n1, n2)
        print(f"{n1} : 2 = {uitkomst}")

    first_round = False
