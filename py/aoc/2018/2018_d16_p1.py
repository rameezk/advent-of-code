from aoc.helper import AOC


@AOC.puzzle(2018, 16, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """Before: [3, 2, 1, 1]
# 9 2 1 2
# After:  [3, 2, 2, 1]"""

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

    opcodes = [addr, addi, mulr, muli, banr, bani, borr, bori,
               setr, seti, gtir, gtri, gtrr, eqir, eqri, eqrr]

    sections = data.split('\n\n\n\n')
    samples_text = sections[0]

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

    count = 0
    for before, instruction, after in samples:
        opcode_num, a, b, c = instruction
        matching = 0
        for op in opcodes:
            if op(before, a, b, c) == after:
                matching += 1
        if matching >= 3:
            count += 1

    print(count)
    AOC.submit_answer(count)


if __name__ == "__main__":
    solve()
