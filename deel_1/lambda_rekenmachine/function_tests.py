import test_lib
import functions
import calculations

# tests voor de lambda rekenmachine functies

test_lib.test('addition', 5, functions.addition(2, 3))
test_lib.test('subtraction', 1, functions.subtraction(3, 2))
test_lib.test('multiplication', 12, functions.multiplication(3, 4))
test_lib.test('division', 2, functions.division(6, 3))

test_lib.report()
