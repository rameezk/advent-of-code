from aoc.helper import AOC


@AOC.puzzle(2022, 6, 1)
def solve():
    data = AOC.get_data().strip()

    for i in range(len(data) - 3):
        window = data[i:i+4]
        if len(set(window)) == 4:
            result = i + 4
            print(result)
            AOC.submit_answer(result)
            break


if __name__ == "__main__":
    solve()
