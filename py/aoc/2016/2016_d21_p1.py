from aoc.helper import AOC


@AOC.puzzle(2016, 21, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """swap position 4 with position 0
# swap letter d with letter b
# reverse positions 0 through 4
# rotate left 1 step
# move position 1 to position 4
# move position 3 to position 0
# rotate based on position of letter b
# rotate based on position of letter d""".splitlines()

    password = "abcdefgh"

    password = list(password)

    for line in data:
        parts = line.split()

        if line.startswith("swap position"):
            x = int(parts[2])
            y = int(parts[5])
            password[x], password[y] = password[y], password[x]

        elif line.startswith("swap letter"):
            x = parts[2]
            y = parts[5]
            for i in range(len(password)):
                if password[i] == x:
                    password[i] = y
                elif password[i] == y:
                    password[i] = x

        elif line.startswith("rotate left"):
            steps = int(parts[2])
            steps = steps % len(password)
            password = password[steps:] + password[:steps]

        elif line.startswith("rotate right") and "based" not in line:
            steps = int(parts[2])
            steps = steps % len(password)
            password = password[-steps:] + password[:-steps]

        elif line.startswith("rotate based"):
            letter = parts[6]
            index = password.index(letter)
            steps = 1 + index
            if index >= 4:
                steps += 1
            steps = steps % len(password)
            password = password[-steps:] + password[:-steps]

        elif line.startswith("reverse"):
            x = int(parts[2])
            y = int(parts[4])
            password[x:y+1] = password[x:y+1][::-1]

        elif line.startswith("move"):
            x = int(parts[2])
            y = int(parts[5])
            char = password.pop(x)
            password.insert(y, char)

    result = ''.join(password)
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
