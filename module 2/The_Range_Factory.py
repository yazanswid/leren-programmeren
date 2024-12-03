aantal = int(input("Hoeveel lijstjes wil je genereren? "))
lengte = int(input("Wat moet de lengte van elk lijstje zijn? "))

for i in range(1, aantal + 1):
    lijstje = list(range(i, i + lengte * i, i))
    print(f"Lijstje {i}: {lijstje}")