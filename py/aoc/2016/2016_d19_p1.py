from aoc.helper import AOC


@AOC.puzzle(2016, 19, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """5"""

    n = int(data)

    power_of_2 = 1
    while power_of_2 * 2 <= n:
        power_of_2 *= 2

    l = n - power_of_2
    winner = 2 * l + 1

    print(winner)
    AOC.submit_answer(winner)


if __name__ == "__main__":
    solve()
