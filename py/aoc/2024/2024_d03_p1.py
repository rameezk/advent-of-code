from aoc.helper import AOC


@AOC.puzzle(year=2024, day=3, part=1)
def solve():
    data = AOC.get_data()
    print(data)

    answer = 0
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
