from aoc.helper import AOC


@AOC.puzzle(2019, 4, 1)
def solve():
    data = AOC.get_data().strip()

    start, end = map(int, data.split('-'))

    count = 0
    for num in range(start, end + 1):
        s = str(num)

        has_adjacent = False
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                has_adjacent = True
                break

        if not has_adjacent:
            continue

        is_increasing = True
        for i in range(len(s) - 1):
            if int(s[i]) > int(s[i + 1]):
                is_increasing = False
                break

        if is_increasing:
            count += 1

    answer = count
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
