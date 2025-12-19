from aoc.helper import AOC


@AOC.puzzle(2016, 19, 2)
def solve():
    data = AOC.get_data().strip()

#     data = """5"""

    n = int(data)

    power_of_3 = 1
    while power_of_3 * 3 <= n:
        power_of_3 *= 3

    if n == power_of_3:
        winner = n
    elif n <= 2 * power_of_3:
        winner = n - power_of_3
    else:
        winner = 2 * n - 3 * power_of_3

    print(winner)
    AOC.submit_answer(winner)


if __name__ == "__main__":
    solve()
