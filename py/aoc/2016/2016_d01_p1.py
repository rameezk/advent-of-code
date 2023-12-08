from aoc.helper import download_input, submit_answer

if __name__ == "__main__":
    # download_input(2016, 1)

    with open("./2016_d01.txt") as f:
        data = f.read()

    x = 0
    y = 0
    d = 0

    for command in data.strip().split(","):
        command = command.strip()
        direction = command[0]
        by = int(command[1::])

        if direction == "L":
            d = (d - 90) % 360
        else:
            d = (d + 90) % 360

        if d == 0:
            y += by
        elif d == 90:
            x += by
        elif d == 180:
            y -= by
        else:
            x -= by

    result = abs(x) + abs(y)
    print(result)
    submit_answer(2016, 1, 1, result)
