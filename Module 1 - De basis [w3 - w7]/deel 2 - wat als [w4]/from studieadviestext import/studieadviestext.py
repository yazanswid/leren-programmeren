STUDIEDOKTER_TITEL = '''
*********************** STUDIEADVIES ***********************
Ik ga jou helpen met jouw opleiding. Jij krijgt een aantal stellingen te zien.
Voor elke stelling moet je zeggen hoeveel dat bij jou voorkomt. Je kunt steeds 
antwoorden: 0 is 'altijd'; 1 is 'vaak'; 2 is 'regelmatig'; 3 is 'soms'; 4 is 'nooit'.
Het is belangrijk om eerlijk te zijn. Op basis van jouw antwoorden krijg je advies. 
'''
OPTIES = "Kies 0: altijd; 1: vaak; 2: regelmatig; 3: soms; 4: nooit"
AANTAL_WEKEN_VRAAG = 'Hoeveel weken ben je al bezig met de opleiding?'
COMPETENTIE_STELLING_1 = 'Ik voel stress of blokkades bij het maken van programmeeropdrachten.'
COMPETENTIE_STELLING_2 = 'Ik stel programmeeropdrachten en -uitdagingen uit.'
COMPETENTIE_STELLING_3 = 'Ik denk dat ik geen talent heb voor de opleiding.'
COMPETENTIE_STELLING_4 = 'Ik vermijd assessments (CJV) en feedback van kritische docenten. '
COMPETENTIE_STELLING_5 = 'Ik vergelijk mezelf met anderen die beter lijken te zijn.'
COMPETENTIE_STELLING_6 = 'Ik voel geen interesse in nieuwe programmeertechnieken.'
COMPETENTIE_STELLING_7 = 'Ik kopieer code van anderen en lever dat in alsof het helemaal van mij is.'

COMPETENTIE_ADVIES_TITEL = '''
*********************** STUDIEADVIES ***********************'''
COMPETENTIE_ADVIES_ZORGELIJK = '''
Het lijkt erop dat je nog weinig zelfvertrouwen, voldoening en plezier ervaart 
in het leren programmeren. Er zijn altijd mogelijkheden om je te helpen de draad 
op te pakken met de opleiding. Praat met jouw SLB-er over extra begeleiding en oefeningen.
'''
COMPETENTIE_ADVIES_TWIJFELACHTIG = '''
Het lijkt erop dat je af en toe weinig zelfvertrouwen, voldoening of plezier ervaart
in het leren programmeren. Houd je zelfvertrouwen en motivatie in de gaten!
'''
COMPETENTIE_ADVIES_GERUSTSTELLEND = '''
Het lijkt erop dat je voldoende zelfvertrouwen, voldoening en plezier ervaart in
het leren programmeren. Mocht het een keer minder gaan, maak je geen zorgen. Have fun!
'''

 
from studieadviestext import *

def get_user_input(prompt):
    while True:
        try:
            value = int(input(prompt))  
            if value in [0, 1, 2, 3, 4]:
                return value
            else:
                print("Ongeldig antwoord. Kies een van de opties: 0, 1, 2, 3, 4.")
        except ValueError:
            print("Ongeldige invoer. Voer een geheel getal in: 0, 1, 2, 3, 4.")

def main():
   
    print(STUDIEDOKTER_TITEL)

   
    while True:
        try:
            weeks = int(input(AANTAL_WEKEN_VRAAG + " "))  
            break
        except ValueError:
            print("Ongeldige invoer. Voer een geldig getal in voor het aantal weken.")

    
    stellingen = [
        COMPETENTIE_STELLING_1,
        COMPETENTIE_STELLING_2,
        COMPETENTIE_STELLING_3,
        COMPETENTIE_STELLING_4,
        COMPETENTIE_STELLING_5,
    ]
    
  
    if weeks >= 10:
        stellingen.extend([COMPETENTIE_STELLING_6, COMPETENTIE_STELLING_7])

    total_score = 0
    answer_counts = [0, 0, 0, 0, 0]  

    
    for i, stelling in enumerate(stellingen, start=1):
        print(f"\nStelling {i}: {stelling}")
        print(OPTIES)
        
        answer = get_user_input(f"Antwoord voor stelling {i}: ")
        total_score += answer
        answer_counts[answer] += 1

    
    average_score = total_score / len(stellingen)

    
    total_answers = len(stellingen)
    always_or_often = answer_counts[0] + answer_counts[1]  
    always_often_regularly = always_or_often + answer_counts[2]  

    print(COMPETENTIE_ADVIES_TITEL)
    
    if average_score <= 2 or always_or_often > total_answers / 2:
        advies = "zorgelijk"
        advies_text = COMPETENTIE_ADVIES_ZORGELIJK
    elif average_score <= 3 or always_often_regularly > total_answers / 2:
        advies = "twijfelachtig"
        advies_text = COMPETENTIE_ADVIES_TWIJFELACHTIG
    else:
        advies = "geruststellend"
        advies_text = COMPETENTIE_ADVIES_GERUSTSTELLEND

   
    print(f"\nUw resultaten:")
    print(f"Totale score: {total_score}")
    print(f"Gemiddelde score: {average_score:.2f}")
    print(f"Advies: {advies}")
    print(advies_text)

if __name__ == "__main__":
    main()
