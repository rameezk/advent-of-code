from aoc.helper import AOC

@AOC.puzzle(2017, 18, 1)
def solve():
    data = AOC.get_data().strip()
    # data = """set a 1
# add a 2
# mul a a
# mod a 5
# snd a
# set a 0
# rcv a
# jgz a -1
# set a 1
# jgz a -2"""

    instructions = [line.split() for line in data.split('\n')]
    registers = {}
    last_sound = None
    pc = 0

    def get_value(x):
        try:
            return int(x)
        except ValueError:
            return registers.get(x, 0)

    while 0 <= pc < len(instructions):
        inst = instructions[pc]
        op = inst[0]

        if op == 'snd':
            last_sound = get_value(inst[1])
            pc += 1
        elif op == 'set':
            registers[inst[1]] = get_value(inst[2])
            pc += 1
        elif op == 'add':
            registers[inst[1]] = registers.get(inst[1], 0) + get_value(inst[2])
            pc += 1
        elif op == 'mul':
            registers[inst[1]] = registers.get(inst[1], 0) * get_value(inst[2])
            pc += 1
        elif op == 'mod':
            registers[inst[1]] = registers.get(inst[1], 0) % get_value(inst[2])
            pc += 1
        elif op == 'rcv':
            if get_value(inst[1]) != 0:
                answer = last_sound
                AOC.submit_answer(answer)
                return
            pc += 1
        elif op == 'jgz':
            if get_value(inst[1]) > 0:
                pc += get_value(inst[2])
            else:
                pc += 1

if __name__ == "__main__":
    solve()
