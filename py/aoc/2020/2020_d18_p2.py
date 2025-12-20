from aoc.helper import AOC

@AOC.puzzle(2020, 18, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """1 + 2 * 3 + 4 * 5 + 6
# 1 + (2 * 3) + (4 * (5 + 6))
# 2 * 3 + (4 * 5)
# 5 + (8 * 3 + 9 + 3 * 4 * 3)
# 5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))
# ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2""".splitlines()

    def evaluate(expr):
        def eval_expr(s, pos):
            i = pos
            addends = []
            current = 0
            op = '+'

            while i < len(s):
                if s[i] == ' ':
                    i += 1
                elif s[i] == '(':
                    value, i = eval_expr(s, i + 1)
                    if op == '+':
                        current += value
                    else:
                        addends.append(current)
                        current = value
                        op = '+'
                elif s[i] == ')':
                    addends.append(current)
                    result = 1
                    for val in addends:
                        result *= val
                    return result, i + 1
                elif s[i].isdigit():
                    num = 0
                    while i < len(s) and s[i].isdigit():
                        num = num * 10 + int(s[i])
                        i += 1
                    if op == '+':
                        current += num
                    else:
                        addends.append(current)
                        current = num
                        op = '+'
                elif s[i] == '+':
                    op = '+'
                    i += 1
                elif s[i] == '*':
                    op = '*'
                    i += 1
                else:
                    i += 1

            addends.append(current)
            result = 1
            for val in addends:
                result *= val
            return result, i

        result, _ = eval_expr(expr, 0)
        return result

    total = sum(evaluate(line) for line in data)

    AOC.submit_answer(total)

if __name__ == "__main__":
    solve()
