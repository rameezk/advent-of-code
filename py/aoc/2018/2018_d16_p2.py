from aoc.helper import AOC


@AOC.puzzle(2018, 16, 2)
def solve():
    data = AOC.get_data().strip()

    def addr(regs, a, b, c):
        result = regs[:]
        result[c] = regs[a] + regs[b]
        return result

    def addi(regs, a, b, c):
        result = regs[:]
        result[c] = regs[a] + b
        return result

    def mulr(regs, a, b, c):
        result = regs[:]
        result[c] = regs[a] * regs[b]
        return result

    def muli(regs, a, b, c):
        result = regs[:]
        result[c] = regs[a] * b
        return result

    def banr(regs, a, b, c):
        result = regs[:]
        result[c] = regs[a] & regs[b]
        return result

    def bani(regs, a, b, c):
        result = regs[:]
        result[c] = regs[a] & b
        return result

    def borr(regs, a, b, c):
        result = regs[:]
        result[c] = regs[a] | regs[b]
        return result

    def bori(regs, a, b, c):
        result = regs[:]
        result[c] = regs[a] | b
        return result

    def setr(regs, a, b, c):
        result = regs[:]
        result[c] = regs[a]
        return result

    def seti(regs, a, b, c):
        result = regs[:]
        result[c] = a
        return result

    def gtir(regs, a, b, c):
        result = regs[:]
        result[c] = 1 if a > regs[b] else 0
        return result

    def gtri(regs, a, b, c):
        result = regs[:]
        result[c] = 1 if regs[a] > b else 0
        return result

    def gtrr(regs, a, b, c):
        result = regs[:]
        result[c] = 1 if regs[a] > regs[b] else 0
        return result

    def eqir(regs, a, b, c):
        result = regs[:]
        result[c] = 1 if a == regs[b] else 0
        return result

    def eqri(regs, a, b, c):
        result = regs[:]
        result[c] = 1 if regs[a] == b else 0
        return result

    def eqrr(regs, a, b, c):
        result = regs[:]
        result[c] = 1 if regs[a] == regs[b] else 0
        return result

    opcodes = {
        'addr': addr, 'addi': addi, 'mulr': mulr, 'muli': muli,
        'banr': banr, 'bani': bani, 'borr': borr, 'bori': bori,
        'setr': setr, 'seti': seti, 'gtir': gtir, 'gtri': gtri,
        'gtrr': gtrr, 'eqir': eqir, 'eqri': eqri, 'eqrr': eqrr
    }

    sections = data.split('\n\n\n\n')
    samples_text = sections[0]
    program_text = sections[1]

    samples = []
    lines = samples_text.split('\n')
    i = 0
    while i < len(lines):
        if lines[i].startswith('Before:'):
            before_str = lines[i].split('[')[1].split(']')[0]
            before = list(map(int, before_str.split(', ')))

            instruction = list(map(int, lines[i+1].split()))

            after_str = lines[i+2].split('[')[1].split(']')[0]
            after = list(map(int, after_str.split(', ')))

            samples.append((before, instruction, after))
            i += 3
        else:
            i += 1

    possible = {}
    for i in range(16):
        possible[i] = set(opcodes.keys())

    for before, instruction, after in samples:
        opcode_num, a, b, c = instruction
        for op_name, op_func in opcodes.items():
            if op_func(before, a, b, c) != after:
                if op_name in possible[opcode_num]:
                    possible[opcode_num].remove(op_name)

    mapping = {}
    while len(mapping) < 16:
        for num, candidates in possible.items():
            if num not in mapping and len(candidates) == 1:
                op_name = list(candidates)[0]
                mapping[num] = op_name
                for other_num in possible:
                    if other_num != num and op_name in possible[other_num]:
                        possible[other_num].remove(op_name)

    program = []
    for line in program_text.strip().split('\n'):
        program.append(list(map(int, line.split())))

    registers = [0, 0, 0, 0]
    for instruction in program:
        opcode_num, a, b, c = instruction
        op_name = mapping[opcode_num]
        op_func = opcodes[op_name]
        registers = op_func(registers, a, b, c)

    result = registers[0]
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
