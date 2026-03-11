from help import *

RECEIPT_TEXT = '***** SPEELHAL ENTREE VOOR {personen:2} PERSONEN *****'
MAX_TICKETS = 30
MAX_VR_VIP_SEAT_TIME = 45
VR_VIP_SEAT_PRICE_PERIOD = 5
TICKET_PRICE = 7.50
VR_VIP_SEAT_PERIOD_PRICE = 0.37
COLA_PRICE = 2.10
POPCORN_PRICE = 2.89
VAT_CODE_H = 'H'
VAT_CODE_L = 'L'

print("SPEELHAL-ENTREE-KASSA")
if not input_yes_no("Wilt u bestellen? (J/N)\n"):
    exit()

nr_tickets = input_int("Hoeveel personen?", 1, MAX_TICKETS)
vr_vip_ordered = input_yes_no("Ook VR-VIP seats? (J/N)\n")

nr_vr_vip_seats = input_int("Hoeveel VR-VIP seats?", 0, nr_tickets) if vr_vip_ordered else 0
vr_vip_seat_time = input_int("Hoeveel minuten in de VR-VIP-seats?", 5, MAX_VR_VIP_SEAT_TIME) if vr_vip_ordered else 0

nr_cola = input_int("Hoeveel cola?", 0, nr_tickets)
nr_popcorn = input_int("Hoeveel popcorn?", 0, nr_tickets)
vat_invoice = input_yes_no("Wilt u een factuur met BTW-specificatie? (J/N)\n")
company_name = input('Op welke bedrijfsnaam komt de factuur?\n').strip() if vat_invoice else ''
if vat_invoice and not company_name:
    company_name = '........... (zelf invullen)'

total_tickets = round(nr_tickets * TICKET_PRICE, 2)
vr_vip_seat_price = vr_vip_seat_time / VR_VIP_SEAT_PRICE_PERIOD * VR_VIP_SEAT_PERIOD_PRICE
total_vr_vip_seats = round(nr_vr_vip_seats * vr_vip_seat_price, 2)
total_cola = round(nr_cola * COLA_PRICE, 2)
total_popcorn = round(nr_popcorn * POPCORN_PRICE, 2)
total_all = total_tickets + total_vr_vip_seats + total_cola + total_popcorn

if vat_invoice:
    vat_perc_H = get_vat_perc(VAT_CODE_H)
    vat_perc_L = get_vat_perc(VAT_CODE_L)
    total_vat_H = get_vat_from_amount_incl(total_tickets + total_vr_vip_seats, VAT_CODE_H)
    total_vat_L = get_vat_from_amount_incl(total_cola + total_popcorn, VAT_CODE_L)
    total_vat = total_vat_H + total_vat_L

# Bon printen
receipt_text = RECEIPT_TEXT.format(personen=nr_tickets)
print(receipt_text + '\n')
print(f'Factuur voor: {company_name}' if vat_invoice else 'Kassabon')
print('-' * len(receipt_text))
print(f'Tickets                   {nr_tickets:2} x {TICKET_PRICE:2.2f} = {total_tickets:6.2f}')
print(f'VR-vip-seats  {vr_vip_seat_time:3} min {nr_vr_vip_seats:2} x {vr_vip_seat_price:2.2f} = {total_vr_vip_seats:6.2f}')
print(f'Cola                      {nr_cola:2} x {COLA_PRICE:2.2f} = {total_cola:6.2f}')
print(f'Popcorn                   {nr_popcorn:2} x {POPCORN_PRICE:2.2f} = {total_popcorn:6.2f}')
print('.' * len(receipt_text))
print(f'Totaal:                               {total_all:6.2f}')

if vat_invoice:
    print(f'BTW Hoog                          {vat_perc_H:2}% {total_vat_H:6.2f}')
    print(f'BTW Laag                          {vat_perc_L:2}% {total_vat_L:6.2f}')
print('=' * len(receipt_text))
print('Bedankt voor de bestelling, veel plezier!')
