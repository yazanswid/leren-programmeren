def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    if number2 == 0:
        return "Kan niet delen door 0"
    result = number1 / number2
    if isinstance(result, float) and result.is_integer():
        return int(result)
    return result
