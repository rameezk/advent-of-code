from aoc.helper import AOC

@AOC.puzzle(2021, 10, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """[({(<(())[]>[[{[]{<()<>>
# [(()[<>])]({[<{<<[]>>(
# {([(<{}[<>[]}>{[]{[(<()>
# (((({<>}<{<{<>}{[]{[]{}
# [[<[([]))<([[{}[[()]]]
# [{[{({}]{}}([{[{{{}}([]
# {<[[]]>}<{[{[{[]{()[[[]
# [<(<(<(<{}))><([]([]()
# <{([([[(<>()){}]>(<<{{
# <{([{{}}[<[[[<>{}]]]>[]]""".splitlines()

    opening = {'(', '[', '{', '<'}
    closing = {')', ']', '}', '>'}
    pairs = {'(': ')', '[': ']', '{': '}', '<': '>'}
    score_map = {')': 3, ']': 57, '}': 1197, '>': 25137}

    total_score = 0

    for line in data:
        stack = []
        corrupted = False

        for char in line:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if not stack:
                    total_score += score_map[char]
                    corrupted = True
                    break

                last_opening = stack.pop()
                expected_closing = pairs[last_opening]

                if char != expected_closing:
                    total_score += score_map[char]
                    corrupted = True
                    break

    answer = total_score

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
