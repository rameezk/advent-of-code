from aoc.helper import download_input, submit_answer

from collections import defaultdict


if __name__ == "__main__":
    download_input(2023, 10)

    with open("./2023_d10.txt") as f:
        sketch = f.read().strip().splitlines()

    #     sketch = """
    # .....
    # .S-7.
    # .|.|.
    # .L-J.
    # .....
    #     """.strip().splitlines()

    M = defaultdict(lambda: [])
    ps = None
    for r, row in enumerate(sketch):
        for c, col in enumerate(row):
            match col:
                case "S":
                    ps = (r, c)
                case "|":
                    M[(r, c)].extend([(r + 1, c), (r - 1, c)])
                case "-":
                    M[(r, c)].extend([(r, c + 1), (r, c - 1)])
                case "L":
                    M[(r, c)].extend([(r - 1, c), (r, c + 1)])
                case "J":
                    M[(r, c)].extend([(r - 1, c), (r, c - 1)])
                case "7":
                    M[(r, c)].extend([(r + 1, c), (r, c - 1)])
                case "F":
                    M[(r, c)].extend([(r + 1, c), (r, c + 1)])
                case _:
                    continue

    n = []
    for k, v in M.items():
        if ps in v:
            n.append(k)
    M[ps] = n

    way_1 = M[ps][0]
    way_2 = M[ps][1]

    visited_1 = [ps]
    visited_2 = [ps]

    c = 1
    while True:
        c += 1

        visited_1.append(way_1)
        nxt_nodes = M[way_1]
        for nx in nxt_nodes:
            if nx not in visited_1:
                way_1 = nx

        visited_2.append(way_2)
        nxt_nodes = M[way_2]
        for nx in nxt_nodes:
            if nx not in visited_2:
                way_2 = nx

        if way_1 == way_2:
            break

    print(c)
    # submit_answer(2023, 10, 1, c)
