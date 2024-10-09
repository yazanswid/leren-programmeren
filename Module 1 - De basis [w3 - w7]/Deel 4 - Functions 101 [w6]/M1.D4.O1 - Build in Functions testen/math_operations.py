# example:
def increment(nr: float) -> float:
  return nr + 1

def decrement(nr: float) -> float:
  return nr - 1

def add(nr1: float, nr2: float) -> float:
  return nr1 + nr2

def subtract(nr1: float, nr2: float) -> float:
  return nr1 - nr2

def multiply(nr1: float, nr2: float) -> float:
  return nr1 * nr2

def divide(nr1: float, nr2: float) -> float:
   try:
        return nr1 / nr2
   except ZeroDivisionError:
        return None
# decrement() moet het getal verminderd met 1 teruggeven
# add() moet de som teruggeven van 2 getallen
# subtract() moet het verschil teruggeven van 2 getallen
# multiply() moet het product teruggeven van 2 getallen
# divide() moet de deling teruggeven van 2 getallen
# Gebruik exception handling in def divide() (delen door nul?)