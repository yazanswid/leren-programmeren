import random
import string

SPECIAL_CHARACTERS = "@#$%&_?"
PASSWORD_LENGTH = 24
MIDDLE_POSITIONS = {PASSWORD_LENGTH // 2 - 1, PASSWORD_LENGTH // 2}


def choose_counts():
    while True:
        uppercase_count = random.randint(2, 6)
        digit_count = random.randint(4, 7)
        special_count = 3
        lowercase_count = PASSWORD_LENGTH - uppercase_count - digit_count - special_count
        if lowercase_count >= 8:
            return uppercase_count, lowercase_count, digit_count, special_count


def generate_password():
    uppercase_count, lowercase_count, digit_count, special_count = choose_counts()
    password = [None] * PASSWORD_LENGTH

    special_positions = random.sample(list(range(1, PASSWORD_LENGTH - 1)), special_count)
    for pos in special_positions:
        password[pos] = random.choice(SPECIAL_CHARACTERS)

    uppercase_positions = random.sample(
        [pos for pos in range(PASSWORD_LENGTH) if pos not in MIDDLE_POSITIONS and password[pos] is None],
        uppercase_count,
    )
    for pos in uppercase_positions:
        password[pos] = random.choice(string.ascii_uppercase)

    digit_positions = random.sample(
        [pos for pos in range(3, PASSWORD_LENGTH) if password[pos] is None],
        digit_count,
    )
    for pos in digit_positions:
        password[pos] = random.choice(string.digits)

    for i in range(PASSWORD_LENGTH):
        if password[i] is None:
            password[i] = random.choice(string.ascii_lowercase)

    if password[-1].islower():
        for i in range(PASSWORD_LENGTH - 1):
            if password[i] in string.ascii_uppercase + string.digits + SPECIAL_CHARACTERS:
                password[i], password[-1] = password[-1], password[i]
                break

    return "".join(password)


if __name__ == "__main__":
    print(generate_password())
