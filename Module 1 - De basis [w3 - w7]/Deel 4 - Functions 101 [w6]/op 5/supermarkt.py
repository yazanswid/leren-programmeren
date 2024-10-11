def round_to_nearest_5_cents(amount):
    """Round the given amount to the nearest 5 cents."""
    return round(amount * 20) / 20  # Rounding logic to the nearest 5 cents

# Test the function with the provided amounts
amounts = [62.60, 76.61, 28.82, 2.23, 28.34, -42.85, 31.06, -138.47, 14.88, 149.69]
for amount in amounts:
    rounded_amount = round_to_nearest_5_cents(amount)
    print(f'€ {amount:.2f} afronden naar € {rounded_amount:.2f}')
