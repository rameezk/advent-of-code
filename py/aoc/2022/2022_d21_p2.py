from aoc.helper import AOC


@AOC.puzzle(2022, 21, 2)
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
        if name == 'humn':
            return None

        value = monkeys[name]
        if isinstance(value, int):
            return value

        parts = value.split()
        left = evaluate(parts[0])
        op = parts[1]
        right = evaluate(parts[2])

        if left is None or right is None:
            return None

        if op == '+':
            return left + right
        elif op == '-':
            return left - right
        elif op == '*':
            return left * right
        elif op == '/':
            return left // right

    def solve_for_target(name, target):
        if name == 'humn':
            return target

        value = monkeys[name]
        parts = value.split()
        left_name = parts[0]
        op = parts[1]
        right_name = parts[2]

        left_val = evaluate(left_name)
        right_val = evaluate(right_name)

        if left_val is None:
            if op == '+':
                new_target = target - right_val
            elif op == '-':
                new_target = target + right_val
            elif op == '*':
                new_target = target // right_val
            elif op == '/':
                new_target = target * right_val
            return solve_for_target(left_name, new_target)
        else:
            if op == '+':
                new_target = target - left_val
            elif op == '-':
                new_target = left_val - target
            elif op == '*':
                new_target = target // left_val
            elif op == '/':
                new_target = left_val // target
            return solve_for_target(right_name, new_target)

    root_parts = monkeys['root'].split()
    left_name = root_parts[0]
    right_name = root_parts[2]

    left_val = evaluate(left_name)
    right_val = evaluate(right_name)

    if left_val is None:
        result = solve_for_target(left_name, right_val)
    else:
        result = solve_for_target(right_name, left_val)

    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
