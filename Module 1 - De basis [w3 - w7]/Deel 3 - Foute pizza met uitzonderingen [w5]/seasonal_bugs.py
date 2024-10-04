print('Welk seizoen vind jij het fijnst?', 
      "A) Lente", 
      "B) Zomer", 
      "C) Herfst", 
      "D) Winter")
gekozen_seizoen = input('? ').lower()

if (gekozen_seizoen == 'a' or gekozen_seizoen == 'c'):
    print('Dus jij vindt een tussenseizoen het fijnst...')
elif (gekozen_seizoen == 'b'):
    weer_type = 'warm'
    print("dus je vindt warme weer fijn")
elif (gekozen_seizoen == 'd'):
    weer_type = 'koud'
    print("dus je houdt van koude weer")
else :
    print(f'Dus jij houd van  weer!')