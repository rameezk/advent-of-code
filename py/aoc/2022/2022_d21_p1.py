from aoc.helper import AOC


@AOC.puzzle(2022, 21, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """root: pppw + sjmn
# dbpl: 5
# cczh: sllz + lgvd
# zczc: 2
# ptdq: humn - dvpt
# dvpt: 3
# lfqf: 4
# humn: 5
# ljgn: 2
# sjmn: drzm * dbpl
# sllz: 4
# pppw: cczh / lfqf
# lgvd: ljgn * ptdq
# drzm: hmdt - zczc
# hmdt: 32""".splitlines()

    monkeys = {}
    for line in data:
        name, job = line.split(': ')
        if job.isdigit() or (job[0] == '-' and job[1:].isdigit()):
            monkeys[name] = int(job)
        else:
            monkeys[name] = job

    def evaluate(name):
        value = monkeys[name]
        if isinstance(value, int):
            return value

        parts = value.split()
        left = evaluate(parts[0])
        op = parts[1]
        right = evaluate(parts[2])

        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return left // right

    result = evaluate('root')
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
