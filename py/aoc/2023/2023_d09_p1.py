from aoc.helper import download_input, submit_answer

from itertools import pairwise


def extrapolate(d: list) -> int:
    s = []
    n = d
    s.append(n)
    while sum(n) != 0:
        n = [r - l for l, r in pairwise(n)]
        s.append(n)

    s.reverse()
    c = 0
    for i in range(1, len(s)):
        last = s[i][-1]
        c += last

    return c


if __name__ == "__main__":
    download_input(2023, 9)

    with open("./2023_d09.txt") as f:
        data = f.read().strip().splitlines()
        data = [list(map(int, d.split())) for d in data]

    #     data = """
    # 0 3 6 9 12 15
    # 1 3 6 10 15 21
    # 10 13 16 21 30 45
    #     """.strip().splitlines()
    #     data = [list(map(int, d.split())) for d in data]

    S = 0
    for d in data:
        e = extrapolate(d)
        S += e

    print(S)
    submit_answer(2023, 9, 1, S)
