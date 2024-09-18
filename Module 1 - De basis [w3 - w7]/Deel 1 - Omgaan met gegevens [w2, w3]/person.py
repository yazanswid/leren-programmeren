def print_address_card(naam, adres, postcode, woonplaats):
    border = '-' * 52
    print(border)
    print(f"|  Naam      : {name.ljust(40)} |")
    print(f"|  Adres     : {address.ljust(40)} |")
    print(f"|  Postcode  : {postal_code.ljust(40)} |")
    print(f"|  Woonplaats: {city.ljust(40)} |")
    print(border)

name = "Fabian van Zandt"
address = "Koekenbakkersplein 23"
postal_code = "2834 EF"
city = "Houten"


print_address_card(name, address, postal_code, city)