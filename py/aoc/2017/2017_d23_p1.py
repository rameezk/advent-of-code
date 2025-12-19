from aoc.helper import AOC

@AOC.puzzle(2017, 23, 1)
def solve():
    data = AOC.get_data().strip()

    instructions = []
    for line in data.split('\n'):
        parts = line.split()
        instructions.append(parts)

    registers = {chr(i): 0 for i in range(ord('a'), ord('h') + 1)}

    def get_value(x):
        if x.lstrip('-').isdigit():
            return int(x)
        return registers[x]

    pc = 0
    mul_count = 0

    while 0 <= pc < len(instructions):
        inst = instructions[pc]
        cmd = inst[0]

        if cmd == 'set':
            registers[inst[1]] = get_value(inst[2])
        elif cmd == 'sub':
            registers[inst[1]] -= get_value(inst[2])
        elif cmd == 'mul':
            registers[inst[1]] *= get_value(inst[2])
            mul_count += 1
        elif cmd == 'jnz':
            if get_value(inst[1]) != 0:
                pc += get_value(inst[2])
                continue

        pc += 1

    answer = mul_count
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
