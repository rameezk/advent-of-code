from aoc.helper import download_input

if __name__ == "__main__":
    # download_input(2015, 1)

    with open("./2015_d01.txt") as f:
        commands = f.read().strip()

    floor = 0
    for command in commands:
        if command == "(":
            floor += 1
        else:
            floor -= 1

    print(floor)
