from aoc.helper import AOC


@AOC.puzzle(2024, 17, 2)
def solve():
    data = AOC.get_data().strip().split('\n\n')

#     data = """Register A: 2024
# Register B: 0
# Register C: 0
#
# Program: 0,3,5,4,3,0""".strip().split('\n\n')

    registers_text = data[0].splitlines()
    reg_b = int(registers_text[1].split(': ')[1])
    reg_c = int(registers_text[2].split(': ')[1])

    program_text = data[1].split(': ')[1]
    program = list(map(int, program_text.split(',')))

    def run_program(a_init):
        reg_a = a_init
        reg_b_local = reg_b
        reg_c_local = reg_c

        def get_combo_value(operand):
            if operand <= 3:
                return operand
            elif operand == 4:
                return reg_a
            elif operand == 5:
                return reg_b_local
            elif operand == 6:
                return reg_c_local

        ip = 0
        output = []

        while ip < len(program):
            opcode = program[ip]
            operand = program[ip + 1]

            if opcode == 0:
                combo = get_combo_value(operand)
                reg_a = reg_a // (2 ** combo)
                ip += 2
            elif opcode == 1:
                reg_b_local = reg_b_local ^ operand
                ip += 2
            elif opcode == 2:
                combo = get_combo_value(operand)
                reg_b_local = combo % 8
                ip += 2
            elif opcode == 3:
                if reg_a != 0:
                    ip = operand
                else:
                    ip += 2
            elif opcode == 4:
                reg_b_local = reg_b_local ^ reg_c_local
                ip += 2
            elif opcode == 5:
                combo = get_combo_value(operand)
                output.append(combo % 8)
                ip += 2
            elif opcode == 6:
                combo = get_combo_value(operand)
                reg_b_local = reg_a // (2 ** combo)
                ip += 2
            elif opcode == 7:
                combo = get_combo_value(operand)
                reg_c_local = reg_a // (2 ** combo)
                ip += 2

        return output

    def find_a(target, a=0):
        if not target:
            return a

        for i in range(8):
            candidate = (a << 3) | i
            output = run_program(candidate)
            if output and output[0] == target[-1]:
                result = find_a(target[:-1], candidate)
                if result is not None:
                    return result
        return None

    result = find_a(program)
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
