from aoc.helper import AOC


@AOC.puzzle(2024, 17, 1)
def solve():
    data = AOC.get_data().strip().split('\n\n')

#     data = """Register A: 729
# Register B: 0
# Register C: 0
#
# Program: 0,1,5,4,3,0""".strip().split('\n\n')

    registers_text = data[0].splitlines()
    reg_a = int(registers_text[0].split(': ')[1])
    reg_b = int(registers_text[1].split(': ')[1])
    reg_c = int(registers_text[2].split(': ')[1])

    program_text = data[1].split(': ')[1]
    program = list(map(int, program_text.split(',')))

    def get_combo_value(operand, a, b, c):
        if operand <= 3:
            return operand
        elif operand == 4:
            return a
        elif operand == 5:
            return b
        elif operand == 6:
            return c
        else:
            raise ValueError("Invalid combo operand")

    ip = 0
    output = []

    while ip < len(program):
        opcode = program[ip]
        operand = program[ip + 1]

        if opcode == 0:
            combo = get_combo_value(operand, reg_a, reg_b, reg_c)
            reg_a = reg_a // (2 ** combo)
            ip += 2
        elif opcode == 1:
            reg_b = reg_b ^ operand
            ip += 2
        elif opcode == 2:
            combo = get_combo_value(operand, reg_a, reg_b, reg_c)
            reg_b = combo % 8
            ip += 2
        elif opcode == 3:
            if reg_a != 0:
                ip = operand
            else:
                ip += 2
        elif opcode == 4:
            reg_b = reg_b ^ reg_c
            ip += 2
        elif opcode == 5:
            combo = get_combo_value(operand, reg_a, reg_b, reg_c)
            output.append(combo % 8)
            ip += 2
        elif opcode == 6:
            combo = get_combo_value(operand, reg_a, reg_b, reg_c)
            reg_b = reg_a // (2 ** combo)
            ip += 2
        elif opcode == 7:
            combo = get_combo_value(operand, reg_a, reg_b, reg_c)
            reg_c = reg_a // (2 ** combo)
            ip += 2

    result = ','.join(map(str, output))
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
