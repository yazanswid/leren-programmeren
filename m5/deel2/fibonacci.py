def fibonacci(aantal):
    reeks = [0, 1]

    for i in range(2, aantal):
        volgende_getal = reeks[i-1] + reeks[i-2]
        reeks.append(volgende_getal)

    return reeks[:aantal]


def bereken_gulden_snede(reeks):
    verhoudingen = []

    for i in range(len(reeks) - 1):
        verhouding = reeks[i] / reeks[i+1]
        verhoudingen.append(verhouding)

    return verhoudingen


def toon_resultaat(aantal):
    fibonacci_list = fibonacci(aantal)
    gulden_snede = bereken_gulden_snede(fibonacci_list)

    print("Fibonacci reeks:")
    print(fibonacci_list)

    print("Gulden snede verhoudingen:")
    print(gulden_snede)



toon_resultaat(10)