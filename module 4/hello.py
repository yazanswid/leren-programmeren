def hello_from_function_town(x):
    lines = []
    for i in range(1, x + 1):
        lines.append(f"Hello from function town {i}!")
    return "\n".join(lines)

# aanroepen van de functie
result = hello_from_function_town(7)
print(result)