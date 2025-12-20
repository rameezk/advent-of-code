from aoc.helper import AOC


@AOC.puzzle(2018, 21, 2)
def solve():
    seen = set()
    last_value = None

    r3 = 0

    while True:
        r5 = r3 | 65536
        r3 = 15028787

        while True:
            r2 = r5 & 255
            r3 = r3 + r2
            r3 = r3 & 16777215
            r3 = r3 * 65899
            r3 = r3 & 16777215

            if 256 > r5:
                if r3 in seen:
                    print(last_value)
                    AOC.submit_answer(last_value)
                    return
                seen.add(r3)
                last_value = r3
                break
            else:
                r5 = r5 // 256


if __name__ == "__main__":
    solve()
