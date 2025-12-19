from aoc.helper import AOC


def increment_password(password):
    chars = list(password)
    i = len(chars) - 1

    while i >= 0:
        if chars[i] == 'z':
            chars[i] = 'a'
            i -= 1
        else:
            chars[i] = chr(ord(chars[i]) + 1)
            break

    return ''.join(chars)


def has_increasing_straight(password):
    for i in range(len(password) - 2):
        if ord(password[i+1]) == ord(password[i]) + 1 and ord(password[i+2]) == ord(password[i]) + 2:
            return True
    return False


def has_forbidden_letters(password):
    return 'i' in password or 'o' in password or 'l' in password


def has_two_pairs(password):
    pairs = []
    i = 0
    while i < len(password) - 1:
        if password[i] == password[i+1]:
            pairs.append(password[i])
            i += 2
        else:
            i += 1
    return len(pairs) >= 2


def is_valid_password(password):
    return (has_increasing_straight(password) and
            not has_forbidden_letters(password) and
            has_two_pairs(password))


def find_next_password(current):
    password = increment_password(current)
    while not is_valid_password(password):
        password = increment_password(password)
    return password


@AOC.puzzle(2015, 11, 2)
def solve():
    data = AOC.get_data().strip()

    first_password = find_next_password(data)
    result = find_next_password(first_password)

    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
