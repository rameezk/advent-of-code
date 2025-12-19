from aoc.helper import AOC


@AOC.puzzle(2016, 12, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """cpy 41 a
# inc a
# inc a
# dec a
# jnz a 2
# dec a""".splitlines()

    registers = {'a': 0, 'b': 0, 'c': 0, 'd': 0}

    instructions = []
    for line in data:
        parts = line.strip().split()
        instructions.append(parts)

    pc = 0
    while pc < len(instructions):
        inst = instructions[pc]
        cmd = inst[0]

        if cmd == 'cpy':
            x = inst[1]
            y = inst[2]
            if x.isdigit() or (x[0] == '-' and x[1:].isdigit()):
                registers[y] = int(x)
            else:
                registers[y] = registers[x]
            pc += 1
        elif cmd == 'inc':
            x = inst[1]
            registers[x] += 1
            pc += 1
        elif cmd == 'dec':
            x = inst[1]
            registers[x] -= 1
            pc += 1
        elif cmd == 'jnz':
            x = inst[1]
            y = inst[2]
            if x.isdigit() or (x[0] == '-' and x[1:].isdigit()):
                x_val = int(x)
            else:
                x_val = registers[x]

            if x_val != 0:
                pc += int(y)
            else:
                pc += 1

    result = registers['a']
    print(f"Register a: {result}")
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
