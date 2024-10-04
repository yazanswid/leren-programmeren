
small_price = 6.50
medium_price = 9.30
large_price = 11.10

def get_pizza_aantal(grootte):
    while True:
        try:
            aantal = int(input(f"Hoeveel {grootte} pizza's wilt u? "))
            if aantal >= 0:
                return aantal
            else:
                print("Het aantal moet positief zijn. Probeer het opnieuw.")
        except ValueError:
            print("Ongeldige invoer! Voer een heel getal in.")


small_pizzas = get_pizza_aantal("small")
medium_pizzas = get_pizza_aantal("medium")
large_pizzas = get_pizza_aantal("large")


small_pizzas = int(input("Hoeveel small pizza's wilt u? "))
medium_pizzas = int(input("Hoeveel medium pizza's wilt u? "))
large_pizzas = int(input("Hoeveel large pizza's wilt u? "))

small_total = small_pizzas * small_price
medium_total = medium_pizzas * medium_price
large_total = large_pizzas * large_price
total = small_total + medium_total + large_total

print("************ KASSA BON ************")
print(f"Pizza's small:  {small_pizzas} * {small_price:.2f} = {small_total:.2f}")
print(f"Pizza's medium: {medium_pizzas} * {medium_price:.2f} = {medium_total:.2f}")
print(f"Pizza's large:  {large_pizzas} * {large_price:.2f} = {large_total:.2f}")
print("----------------------------------")
print(f"Te betalen: {total:.2f}")



