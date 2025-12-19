from aoc.helper import AOC


@AOC.puzzle(2016, 23, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """cpy 2 a
# tgl a
# tgl a
# tgl a
# cpy 1 a
# dec a
# dec a""".splitlines()

    instructions = [line.split() for line in data]
    registers = {'a': 7, 'b': 0, 'c': 0, 'd': 0}
    pc = 0

    def get_value(x):
        if x.lstrip('-').isdigit():
            return int(x)
        return registers[x]

    while pc < len(instructions):
        inst = instructions[pc]
        cmd = inst[0]

        if cmd == 'cpy':
            x, y = inst[1], inst[2]
            if y in registers:
                registers[y] = get_value(x)
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
            if get_value(x) != 0:
                pc += get_value(y)
            else:
                pc += 1
        elif cmd == 'tgl':
            x = inst[1]
            target = pc + get_value(x)
            if 0 <= target < len(instructions):
                target_inst = instructions[target]
                if len(target_inst) == 2:
                    if target_inst[0] == 'inc':
                        target_inst[0] = 'dec'
                    else:
                        target_inst[0] = 'inc'
                else:
                    if target_inst[0] == 'jnz':
                        target_inst[0] = 'cpy'
                    else:
                        target_inst[0] = 'jnz'
            pc += 1

    print(f"Register a: {registers['a']}")
    AOC.submit_answer(registers['a'])
    return registers['a']


if __name__ == "__main__":
    solve()
