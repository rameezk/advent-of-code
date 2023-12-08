from aoc.helper import submit_answer

if __name__ == "__main__":
    with open("./2015_d01.txt") as f:
        commands = f.read().strip()

    floor = 0
    pos = 0
    for idx, command in enumerate(commands, start=1):
        if command == "(":
            floor += 1
        else:
            floor -= 1

        if floor == -1:
            pos = idx
            break

    print(pos)
    # submit_answer(2015, 1, 2, pos)
