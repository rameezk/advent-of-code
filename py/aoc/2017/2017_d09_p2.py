from aoc.helper import AOC

@AOC.puzzle(2017, 9, 2)
def solve():
    data = AOC.get_data().strip()

    garbage_count = 0
    in_garbage = False
    i = 0

    while i < len(data):
        char = data[i]

        if in_garbage:
            if char == '!':
                i += 2
                continue
            elif char == '>':
                in_garbage = False
            else:
                garbage_count += 1
        else:
            if char == '<':
                in_garbage = True

        i += 1

    answer = garbage_count
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
