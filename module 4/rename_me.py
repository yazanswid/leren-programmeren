def is_even(getal:int) -> bool:
    return getal % 2 == 0

print(is_even(int(input("Voer een getal in: ")))) 




def keer_woorden_om(zin:str) -> str:
    woorden = zin.split()
    omgekeerde_woorden = woorden[::-1]
    omgekeerde_zin = ' '.join(omgekeerde_woorden)
    return omgekeerde_zin

print(keer_woorden_om(input("Voer een zin in: ")))  




def unieke_tekens_teller(tekens:str) -> int:
    uniek_tekens = set(tekens)
    tekens_tellen = len(uniek_tekens)
    return tekens_tellen

print(unieke_tekens_teller(input("Voer een zin in: ")))

def tekens_teller(zin:str) -> float:
    worden = zin.split()
    
    tekens = 0
    for letters in worden:
        tekens += len(letters)

    resultaat = tekens / len(worden)
    return resultaat

print(tekens_teller(input("Voer een zin in: ")))


def cijfer_tafel(getal:int, tot_en_met:int=10) -> None:
    for vermenigvuldegir in range(1, tot_en_met+1):
        resultaat = vermenigvuldegir * getal
        print(f'{vermenigvuldegir} x {getal} = {resultaat}')

print(cijfer_tafel(int(input("Voer een getal in: ")))) 