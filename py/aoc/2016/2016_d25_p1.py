from aoc.helper import AOC


@AOC.puzzle(2016, 25, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

    instructions = [line.split() for line in data]

    def get_value(x, registers):
        if x.lstrip('-').isdigit():
            return int(x)
        return registers[x]

    def run_program(initial_a, max_outputs=50):
        registers = {'a': initial_a, 'b': 0, 'c': 0, 'd': 0}
        pc = 0
        outputs = []

        while pc < len(instructions) and len(outputs) < max_outputs:
            inst = instructions[pc]
            cmd = inst[0]

            if cmd == 'cpy':
                x, y = inst[1], inst[2]
                if y in registers:
                    registers[y] = get_value(x, registers)
                pc += 1
            elif cmd == 'inc':
                x = inst[1]
                if x in registers:
                    registers[x] += 1
                pc += 1
            elif cmd == 'dec':
                x = inst[1]
                if x in registers:
                    registers[x] -= 1
                pc += 1
            elif cmd == 'jnz':
                x, y = inst[1], inst[2]
                if get_value(x, registers) != 0:
                    pc += get_value(y, registers)
                else:
                    pc += 1
            elif cmd == 'out':
                x = inst[1]
                output = get_value(x, registers)
                outputs.append(output)
                pc += 1

        return outputs

    def is_clock_signal(outputs):
        if len(outputs) < 2:
            return False
        for i in range(len(outputs)):
            expected = i % 2
            if outputs[i] != expected:
                return False
        return True

    a = 1
    while True:
        outputs = run_program(a)
        if is_clock_signal(outputs):
            print(f"Found answer: {a}")
            print(f"Outputs: {outputs[:20]}")
            AOC.submit_answer(a)
            return a
        a += 1
        if a > 10000:
            print("No solution found in reasonable range")
            break


if __name__ == "__main__":
    solve()
