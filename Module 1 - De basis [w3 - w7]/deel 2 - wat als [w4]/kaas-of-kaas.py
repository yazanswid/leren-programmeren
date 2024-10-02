
def stel_vraag(vraag):
    antwoord = input(vraag + " (ja/nee): ").lower()
    while antwoord not in ["ja", "nee"]:
        antwoord = input("Geef alstublieft een geldig antwoord (ja/nee): ").lower()
    return antwoord == "ja"


def identificeer_kaas():
    if stel_vraag("Is de kaas geel?"):
        if stel_vraag("Zitten er gaten in?"):
            if stel_vraag("Is de kaas belachelijk duur?"):
                print("De kaas is Emmenthaler.")
            else:
                print("De kaas is Leerdammer.")
        else:
            if stel_vraag("Is de kaas hard als steen?"):
                print("De kaas is Parmigiano Reggiano")
            else:
                print("De kaas is Goudse kaas.")
    else:
        if stel_vraag("Heeft de kaas blauwe schimmel?"):
            if stel_vraag("Heeft de kaas een korst?"):
                print("De kaas is Blue de Rochbaron.")
            else:
                print("De kaas is Fourme d'Ambert.")
        else:
            if stel_vraag("Heeft de kaas een korst?"):
                print("De kaas is Camembert.")
            else:
                print("De kaas is Mozzarella.")

identificeer_kaas()
