from aoc.helper import AOC

@AOC.puzzle(2021, 10, 2)
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
    score_map = {')': 1, ']': 2, '}': 3, '>': 4}

    scores = []

    for line in data:
        stack = []
        corrupted = False

        for char in line:
            if char in opening:
                stack.append(char)
            elif char in closing:
                if not stack:
                    corrupted = True
                    break

                last_opening = stack.pop()
                expected_closing = pairs[last_opening]

                if char != expected_closing:
                    corrupted = True
                    break

        if not corrupted and stack:
            completion = []
            while stack:
                last_opening = stack.pop()
                completion.append(pairs[last_opening])

            line_score = 0
            for char in completion:
                line_score = line_score * 5 + score_map[char]

            scores.append(line_score)

    scores.sort()
    answer = scores[len(scores) // 2]

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
