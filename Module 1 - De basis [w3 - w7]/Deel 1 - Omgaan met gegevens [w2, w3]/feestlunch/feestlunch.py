
aantal_croissantjes = 17
prijs_per_croissantje = 0.39


aantal_stokbroden = 2
prijs_per_stokbrood = 2.78


kortingsbonnen = 3
waarde_per_kortingsbon = 0.50


totale_kosten_croissantjes = aantal_croissantjes * prijs_per_croissantje
totale_kosten_stokbroden = aantal_stokbroden * prijs_per_stokbrood


totale_kosten = totale_kosten_croissantjes + totale_kosten_stokbroden


totale_korting = kortingsbonnen * waarde_per_kortingsbon

te_betalen = totale_kosten - totale_korting


print(f"Het totale bedrag dat je moet betalen is: €{te_betalen:.2f}")
