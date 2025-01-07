
vertalingen = {
    "zon": "maan",
    "dag": "nacht",
    "lachen": "huilen",
    "bloem": "paddenstoel",
    "vogel": "vis",
    "vliegen": "zwemmen",
    "bos": "woestijn",
    "berg": "vallei",
    "rivier": "woestijn",
    "regen": "zonneschijn"
}

def vertaal_tekst(tekst):
    woorden = tekst.split()
    vertaalde_woorden = []
    
    for woord in woorden:
        
        schoon_woord = woord.strip(".,!?")
        
        
        if schoon_woord.lower() in vertalingen:
            vertaald_woord = vertalingen[schoon_woord.lower()]
            
            
            if schoon_woord.istitle():
                vertaald_woord = vertaald_woord.capitalize()
            
            
            if woord[-1] in ".,!?":
                vertaald_woord += woord[-1]
            
            vertaalde_woorden.append(vertaald_woord)
        else:
            vertaalde_woorden.append(woord)
    
    return " ".join(vertaalde_woorden)


print("Welkom bij het vertaalprogramma!")
invoer = input("Voer een stukje tekst in om te vertalen: ")

vertaalde_tekst = vertaal_tekst(invoer)
print("\nVertaalde tekst:")
print(vertaalde_tekst)