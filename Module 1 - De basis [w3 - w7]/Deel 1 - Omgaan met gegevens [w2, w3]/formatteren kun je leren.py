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


print(f'De feestlunch kost je bij de bakker {colored(te_betalen, "blue")} euro voor de {colored(aantal_croissantjes, "cyan")} croissantjes en de {colored(aantal_stokbroden, "cyan")} stokbroden als de {colored(kortingsbonnen, "green")} kortingsbonnen nog geldig zijn!')


toegangticket_per_persoon = 7.45
aantal_per = 4

vr_vip_min_5 = 0.37
vr_vip_tijd = 45

kosten_ticket_per = toegangticket_per_persoon * aantal_per

kosten_vr = ( vr_vip_tijd / 5 ) * vr_vip_min_5 * aantal_per

totalekosten = kosten_ticket_per + kosten_vr

print(f'Dit geweldige dagje-uit met {colored(aantal_per, "light_magenta")} mensen in de Speelhal met {colored(vr_vip_tijd, "light_magenta")} minuten VR kost je maar {colored(totalekosten, "light_red")} euro')
