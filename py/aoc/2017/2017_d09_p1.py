from aoc.helper import AOC

@AOC.puzzle(2017, 9, 1)
def solve():
    data = AOC.get_data().strip()

    total_score = 0
    depth = 0
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
            if char == '<':
                in_garbage = True
            elif char == '{':
                depth += 1
                total_score += depth
            elif char == '}':
                depth -= 1

        i += 1

    answer = total_score
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
