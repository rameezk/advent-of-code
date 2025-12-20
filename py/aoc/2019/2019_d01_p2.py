from aoc.helper import AOC


@AOC.puzzle(2019, 1, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """14
# 1969
# 100756""".splitlines()

    def calculate_fuel(mass):
        fuel = mass // 3 - 2
        if fuel <= 0:
            return 0
        return fuel + calculate_fuel(fuel)

    answer = sum(calculate_fuel(int(mass)) for mass in data)
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
