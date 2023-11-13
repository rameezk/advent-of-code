from aoc.helper import download_input, submit_answer

import re


def get_adj(x, y, max_x, max_y):
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            nx = x + dx
            ny = y + dy

            if nx < 0 or ny < 0:
                continue
            if nx > max_x or ny > max_y:
                continue

            if nx == x and ny == y:
                continue

            yield nx, ny


def get_number(E, r, c, max_, V: set) -> int:
    if f"{r},{c}" in V:
        return 0

    V.add(f"{r},{c}")
    n = E[f"{r},{c}"]
    for i in range(c - 1, -1, -1):
        t = E[f"{r},{i}"]
        if not t.isdigit():
            break
        V.add(f"{r},{i}")
        n = t + n
    for i in range(c + 1, max_):
        t = E[f"{r},{i}"]
        if not t.isdigit():
            break
        V.add(f"{r},{i}")
        n = n + t
    return int(n)


if __name__ == "__main__":
    # download_input(2023, 3)

    with open("./2023_d03.txt") as f:
        engine = f.read().strip().splitlines()

    #     engine = """
    # 467..114..
    # ...*......
    # ..35..633.
    # ......#...
    # 617*......
    # .....+.58.
    # ..592.....
    # ......755.
    # ...$.*....
    # .664.598..
    #     """.strip().splitlines()

    E = {}
    S = []
    max_y = len(engine)
    max_x = len(engine[0])
    V = set()
    for r, line in enumerate(engine):
        for c, char in enumerate(list(line)):
            E[f"{r},{c}"] = char

            if not char.isdigit() and char != ".":
                S.append([r, c])

    T = 0
    for s in S:
        for r, c in get_adj(s[0], s[1], max_x, max_y):
            coord = f"{r},{c}"
            if coord in E and E[coord].isdigit():
                n = get_number(E, r, c, max_x, V)
                T += n

    print(T)
    # submit_answer(2023, 3, 1, T)
