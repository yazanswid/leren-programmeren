import random

def guess_the_number():
    total_score = 0
    rounds = 0
    
    print("Welkom bij het getalraadspel!")
    
    while rounds < 20:
        secret_number = random.randint(1, 1000)
        attempts = 0
        round_score = 0
        
        print(f"\nRonde {rounds + 1}: Ik heb een nieuw getal gekozen tussen 1 en 1000.")
        
        while attempts < 10:
            try:
                guess = int(input(f"Poging {attempts + 1}: Voer je gok in: "))
            except ValueError:
                print("Ongeldige invoer. Voer een geheel getal in.")
                continue
            
            if guess < 1 or guess > 1000:
                print("Je gok moet tussen 1 en 1000 liggen.")
                continue
            
            attempts += 1
            
            if guess < secret_number:
                print("Te laag! Probeer opnieuw.")
            elif guess > secret_number:
                print("Te hoog! Probeer opnieuw.")
            else:
                round_score += 1
                print(f"Gefeliciteerd! Je hebt het juiste getal {secret_number} geraden in {attempts} pogingen.")
                break
            
            
            if abs(guess - secret_number) < 20:
                print("Je bent heel warm!")
            elif abs(guess - secret_number) < 50:
                print("Je bent warm!")
        
        
        if round_score > 0:
            total_score += 1
        
        print(f"Ronde {rounds + 1} is voorbij. Je score in deze ronde: {round_score}")
        print(f"Tot nu toe heb je {total_score} punt(en).")
        
        
        rounds += 1
        if rounds < 20:
            continue_game = input("Nog een getal raden? (ja/nee): ").strip().lower()
            if continue_game != "ja":
                break
    
    print(f"\nEinde van het spel! Je eindscore is {total_score} punt(en).")

if __name__ == "__main__":
    guess_the_number()
