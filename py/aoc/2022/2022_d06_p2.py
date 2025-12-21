from aoc.helper import AOC


@AOC.puzzle(2022, 6, 2)
def solve():
    data = AOC.get_data().strip()

    for i in range(len(data) - 13):
        window = data[i:i+14]
        if len(set(window)) == 14:
            result = i + 14
            print(result)
            AOC.submit_answer(result)
            break


if __name__ == "__main__":
    solve()
