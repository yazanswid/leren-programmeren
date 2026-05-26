import sys, os
from test_lib3 import test, report

sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from data import JOURNEY_IN_DAYS

#schrijf je test hier
expected_days = 11
result_days = JOURNEY_IN_DAYS
test('JOURNEY_IN_DAYS - test', expected_days, result_days)


if __name__ == "__main__":
    report()