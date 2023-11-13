from aoc.helper import download_input, submit_answer

if __name__ == "__main__":
    # download_input(2016, 2)

    keypad = [
        ["", "", "1", "", ""],
        ["", "2", "3", "4", ""],
        ["5", "6", "7", "8", "9"],
        ["", "A", "B", "C", ""],
        ["", "", "D", "", ""],
    ]

    with open("./2016_d02.txt") as f:
        instructions = f.read()

    #     instructions = """
    # ULL
    # RRDDD
    # LURDL
    # UUUUD
    #         """

    code = ""
    position = (2, 0)
    for line in instructions.strip().splitlines():
        for command in line:
            x, y = position
            if command == "U":
                if x > 0 and keypad[x - 1][y] != "":
                    x = x - 1
            elif command == "L":
                if y > 0 and keypad[x][y - 1] != "":
                    y = y - 1
            elif command == "R":
                if y < 4 and keypad[x][y + 1] != "":
                    y = y + 1
            else:
                if x < 4 and keypad[x + 1][y] != "":
                    x = x + 1
            position = (x, y)
        digit = keypad[position[0]][position[1]]
        code += digit
    print(code)

    # submit_answer(2016, 2, 2, code)
