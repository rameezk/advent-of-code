from aoc.helper import AOC


@AOC.puzzle(2024, 1, 1)
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

    L = sorted(L)
    R = sorted(R)

    T = 0
    for d1, d2 in zip(L, R):
        T += abs(d1 - d2)

    print(T)
    AOC.submit_answer(T)


if __name__ == "__main__":
    solve()
