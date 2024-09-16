from termcolor import colored, cprint, COLORS

aantal_croissantjes = 17
aantal_stokbroden = 2
prijs_per_stokbrood =  2.78
kortingsbonnen = 3
waarde_per_kortingsbon = 50
prijs_per_croissantje = 0.39

totale_kosten_croissantjes = aantal_croissantjes * prijs_per_croissantje
totale_kosten_stokbroden = aantal_stokbroden * prijs_per_stokbrood


totale_kosten = totale_kosten_croissantjes + totale_kosten_stokbroden


totale_korting = kortingsbonnen * waarde_per_kortingsbon

te_betalen = totale_kosten - totale_korting


print(f"Het totale bedrag dat je moet betalen is: €{colored(te_betalen,'red')}")
