import math


def calculate_cilinder_content(diameter, height):
    radius = diameter / 2
    volume = math.pi * radius ** 2 * height
    return round(volume, 1)


def test(name, expected, calculated):
    success = abs(expected - calculated) < 0.1  
    print(f"{name}: {'Success' if success else 'Fail'} - Expected: {expected}, Calculated: {calculated}")


test_cases = [
    (8.0, 5.0, 251.3),
    (11.0, 7.0, 665.2),
    (18.0, 7.0, 1781.3),
    (15.0, 2.0, 353.4),
    (0.0, 6.0, 0.0)
]


for diameter, height, expected_content in test_cases:
    calculated_content = calculate_cilinder_content(diameter, height)
    test_name = f"test diameter: {diameter} height: {height}"
    test(test_name, expected_content, calculated_content)


def report():
    print("All tests completed.")

report()