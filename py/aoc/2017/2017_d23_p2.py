from aoc.helper import AOC

@AOC.puzzle(2017, 23, 2)
def solve():
    data = AOC.get_data().strip()

    b = 57
    c = b
    b = b * 100 + 100000
    c = b + 17000

    h = 0
    for b_val in range(b, c + 1, 17):
        f = 1
        for d in range(2, b_val):
            if b_val % d == 0:
                f = 0
                break
        if f == 0:
            h += 1

    answer = h
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
