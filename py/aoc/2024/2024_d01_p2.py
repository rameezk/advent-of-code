from aoc.helper import AOC


@AOC.puzzle(2024, 1, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

    #     data = """3   4
    # 4   3
    # 2   5
    # 1   3
    # 3   9
    # 3   3""".strip().splitlines()

    L = []
    R = []

    for line in data:
        l, r = line.split()
        L.append(int(l))
        R.append(int(r))

    S = 0
    for d in L:
        c = R.count(d)
        S += c * d

    print(S)
    AOC.submit_answer(S)


if __name__ == "__main__":
    solve()
