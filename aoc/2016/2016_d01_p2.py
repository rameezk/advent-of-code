from aoc.helper import download_input, submit_answer

if __name__ == "__main__":
    # download_input(2016, 1)

    with open("./2016_d01.txt") as f:
        data = f.read()

    # data = "R8, R4, R4, R8"

    x = 0
    y = 0
    d = 0
    visited = []
    already_visited_coord = None
    for command in data.strip().split(","):
        if already_visited_coord is not None:
            break

        command = command.strip()
        direction = command[0]
        by = int(command[1::])

        if direction == "L":
            d = (d - 90) % 360
        else:
            d = (d + 90) % 360

        for i in range(by):
            if d == 0:
                y += 1
            elif d == 90:
                x += 1
            elif d == 180:
                y -= 1
            else:
                x -= 1

            if (x, y) in visited:
                already_visited_coord = (x, y)
                break

            visited.append((x, y))

    distance = abs(already_visited_coord[0]) + abs(already_visited_coord[1])
    print(distance)
    submit_answer(2016, 1, 2, distance)
