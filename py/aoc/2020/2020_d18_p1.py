from aoc.helper import AOC

@AOC.puzzle(2020, 18, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """1 + 2 * 3 + 4 * 5 + 6
# 2 * 3 + (4 * 5)
# 5 + (8 * 3 + 9 + 3 * 4 * 3)
# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
# ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2""".splitlines()

    def evaluate(expr):
        def eval_expr(s, pos):
            result = 0
            op = '+'
            i = pos

            while i < len(s):
                if s[i] == ' ':
                    i += 1
                elif s[i] == '(':
                    value, i = eval_expr(s, i + 1)
                    if op == '+':
                        result += value
                    else:
                        result *= value
                elif s[i] == ')':
                    return result, i + 1
                elif s[i].isdigit():
                    num = 0
                    while i < len(s) and s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1
                    if op == '+':
                        result += num
                    else:
                        result *= num
                elif s[i] in '+*':
                    op = s[i]
                    i += 1
                else:
                    i += 1

            return result, i

        result, _ = eval_expr(expr, 0)
        return result

    total = sum(evaluate(line) for line in data)

    AOC.submit_answer(total)

if __name__ == "__main__":
    solve()
