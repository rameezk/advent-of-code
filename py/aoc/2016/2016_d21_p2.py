from aoc.helper import AOC


@AOC.puzzle(2016, 21, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

    password = "fbgdceah"

    password = list(password)

    for line in reversed(data):
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
            password = password[-steps:] + password[:-steps]

        elif line.startswith("rotate right") and "based" not in line:
            steps = int(parts[2])
            steps = steps % len(password)
            password = password[steps:] + password[:steps]

        elif line.startswith("rotate based"):
            letter = parts[6]
            current_index = password.index(letter)

            for original_index in range(len(password)):
                steps = 1 + original_index
                if original_index >= 4:
                    steps += 1
                steps = steps % len(password)

                if (original_index + steps) % len(password) == current_index:
                    rotate_back = steps
                    password = password[rotate_back:] + password[:rotate_back]
                    break

        elif line.startswith("reverse"):
            x = int(parts[2])
            y = int(parts[4])
            password[x:y+1] = password[x:y+1][::-1]

        elif line.startswith("move"):
            x = int(parts[2])
            y = int(parts[5])
            char = password.pop(y)
            password.insert(x, char)

    result = ''.join(password)
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
