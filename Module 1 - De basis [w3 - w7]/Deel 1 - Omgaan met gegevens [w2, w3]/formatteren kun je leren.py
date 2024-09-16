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

print(f"‘De feestlunch kost je bij de bakker {te_betalen:.2f} voor de {totale_kosten_croissantjes:.2f} en de {totale_kosten_stokbroden:.f2} als de {totale_korting} nog geldig zijn!’")




toegangticket_per_persoon = 7.45
aantal_per = 4

vr_vip_min_5 = 0.37
vr_vip_tijd = 45

kosten_ticket_per = toegangticket_per_persoon * aantal_per

kosten_vr = ( vr_vip_tijd / 5 ) * vr_vip_min_5 * aantal_per

totalekosten = kosten_ticket_per + kosten_vr

print("‘Dit geweldige dagje-uit {aantal_per} in de Speelhal {vr_vip_tijd} VR kost je maar 44.44 euro’")