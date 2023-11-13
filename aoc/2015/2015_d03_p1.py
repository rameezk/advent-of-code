from aoc.helper import download_input, submit_answer

if __name__ == "__main__":
    # download_input(2015, 3)

    with open("./2015_d03.txt") as f:
        data = f.read().strip()

    # data = "^v^v^v^v^v"

    x = 0
    y = 0
    v = {(0, 0)}
    for d in data:
        if d == ">":
            x += 1
        elif d == "<":
            x -= 1
        elif d == "^":
            y += 1
        else:
            y -= 1

        v.add((x, y))

    h = len(v)
    print(h)
    submit_answer(2015, 3, 1, h)
