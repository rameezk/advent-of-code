from aoc.helper import AOC

@AOC.puzzle(2017, 8, 1)
def solve():
    data = AOC.get_data().strip()
    # data = """b inc 5 if a > 1
# a inc 1 if b < 5
# c dec -10 if a >= 1
# c inc -20 if c == 10"""

    registers = {}

    for line in data.split('\n'):
        parts = line.split()
        reg = parts[0]
        op = parts[1]
        value = int(parts[2])
        cond_reg = parts[4]
        cond_op = parts[5]
        cond_val = int(parts[6])

        if cond_reg not in registers:
            registers[cond_reg] = 0
        if reg not in registers:
            registers[reg] = 0

        condition_met = False
        if cond_op == '>':
            condition_met = registers[cond_reg] > cond_val
        elif cond_op == '<':
            condition_met = registers[cond_reg] < cond_val
        elif cond_op == '>=':
            condition_met = registers[cond_reg] >= cond_val
        elif cond_op == '<=':
            condition_met = registers[cond_reg] <= cond_val
        elif cond_op == '==':
            condition_met = registers[cond_reg] == cond_val
        elif cond_op == '!=':
            condition_met = registers[cond_reg] != cond_val

        if condition_met:
            if op == 'inc':
                registers[reg] += value
            elif op == 'dec':
                registers[reg] -= value

    answer = max(registers.values())
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
