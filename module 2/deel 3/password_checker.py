
correct_password = "geheim123"


attempts = 0


while attempts < 5:
    
    user_input = input("Voer het wachtwoord in: ")
    
    
    attempts += 1
    
    
    if user_input == correct_password:
        print(f"Correct! Je hebt het wachtwoord geraden in {attempts} poging(en).")
        break
    else:
        
        remaining_attempts = 5 - attempts
        if remaining_attempts > 0:
            print(f"Onjuist wachtwoord. Je hebt nog {remaining_attempts} poging(en) over.")
        else:
            print("Je hebt het maximale aantal pogingen bereikt. Je mag niet meer inloggen.")