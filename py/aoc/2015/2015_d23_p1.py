from aoc.helper import AOC


@AOC.puzzle(2015, 23, 1)
def solve():
    data = AOC.get_data().strip()

    sample_data = """inc a
jio a, +2
tpl a
inc a"""

    lines = data.split('\n')

    registers = {'a': 0, 'b': 0}
    pc = 0

    while 0 <= pc < len(lines):
        instruction = lines[pc]
        parts = instruction.replace(',', '').split()

        cmd = parts[0]

        if cmd == 'hlf':
            reg = parts[1]
            registers[reg] //= 2
            pc += 1
        elif cmd == 'tpl':
            reg = parts[1]
            registers[reg] *= 3
            pc += 1
        elif cmd == 'inc':
            reg = parts[1]
            registers[reg] += 1
            pc += 1
        elif cmd == 'jmp':
            offset = int(parts[1])
            pc += offset
        elif cmd == 'jie':
            reg = parts[1]
            offset = int(parts[2])
            if registers[reg] % 2 == 0:
                pc += offset
            else:
                pc += 1
        elif cmd == 'jio':
            reg = parts[1]
            offset = int(parts[2])
            if registers[reg] == 1:
                pc += offset
            else:
                pc += 1

    result = registers['b']
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
