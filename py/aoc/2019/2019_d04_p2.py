from aoc.helper import AOC


@AOC.puzzle(2019, 4, 2)
def solve():
    data = AOC.get_data().strip()

    start, end = map(int, data.split('-'))

    count = 0
    for num in range(start, end + 1):
        s = str(num)

        is_increasing = True
        for i in range(len(s) - 1):
            if int(s[i]) > int(s[i + 1]):
                is_increasing = False
                break

        if not is_increasing:
            continue

        has_exact_double = False
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            if j - i == 2:
                has_exact_double = True
                break
            i = j

        if has_exact_double:
            count += 1

    answer = count
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
