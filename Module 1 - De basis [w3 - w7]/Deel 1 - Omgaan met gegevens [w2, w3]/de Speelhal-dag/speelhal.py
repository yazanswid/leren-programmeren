from termcolor import colored, cprint, COLORS

toegangticket_per_persoon = 7.45
aantal_per = 4

vr_vip_min_5 = 0.37
vr_vip_tijd = 45

kosten_ticket_per = toegangticket_per_persoon * aantal_per

kosten_vr = ( vr_vip_tijd / 5 ) * vr_vip_min_5 * aantal_per

totalekosten = round(kosten_ticket_per + kosten_vr,2)

print(f"de totale kosten voor de speelhalte is {colored(totalekosten,'green')}")