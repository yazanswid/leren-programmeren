#import hier je functie "from [bestandsnaamZonderExtentie] import [functieNaam]"
from test_libe import test, report  # Importing the necessary functions
from Min_en_Max import max_min     # Importing the max_min function to test

# Test 1: Both numbers are equal
expected = 'beide zijn gelijk'
result = max_min(5, 5)  # Testing with two equal numbers
test('TEST nr1=nr2', expected, result)

# Test 2: First number is greater than the second
expected = '7 is groter dan 3'
result = max_min(7, 3)  # Testing where the first number is greater
test('TEST nr1>nr2', expected, result)

# Test 3: First number is smaller than the second
expected = '4 is kleiner dan 8'
result = max_min(4, 8)  # Testing where the first number is smaller
test('TEST nr1<nr2', expected, result)

# Run the report to summarize the results of the tests
if __name__ == "__main__":
    report()
