from aoc.helper import AOC

@AOC.puzzle(2020, 1, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

    numbers = [int(x) for x in data]

    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            if numbers[i] + numbers[j] == 2020:
                answer = numbers[i] * numbers[j]
                print(f"Part 1: {answer}")
                return

if __name__ == "__main__":
    solve()
