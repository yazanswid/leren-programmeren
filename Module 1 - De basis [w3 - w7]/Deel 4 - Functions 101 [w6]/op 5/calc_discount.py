from test_libe import *

month_discount_brands = ["Vespa", "Kymco", "Yamaha"]
MONTH_DISCOUNT_PERC = 10
def calc_discount(price: float, brand: str, month_discount_brands: str) -> float:
    if price < 0:
        return 0.0

    if brand in month_discount_brands:
        discount = (price * MONTH_DISCOUNT_PERC) / 100
    else:
        discount = 0
    return round(discount, 2)

Scooters = [
    (100, "Vespa"),
    (200, "Kymco"), 
    (150, "Yamaha"), 
]

for price, brand in Scooters:
    calculated_discount = calc_discount(price, brand, month_discount_brands)
    test(f'Test met prijs: {price}, merk: {brand}',  round((price * MONTH_DISCOUNT_PERC) / 100, 2), calculated_discount)

report()