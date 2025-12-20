from aoc.helper import AOC


@AOC.puzzle(2018, 19, 1)
def solve():
    data = AOC.get_data().strip()

    def addr(regs, a, b, c):
        regs[c] = regs[a] + regs[b]

    def addi(regs, a, b, c):
        regs[c] = regs[a] + b

    def mulr(regs, a, b, c):
        regs[c] = regs[a] * regs[b]

    def muli(regs, a, b, c):
        regs[c] = regs[a] * b

    def banr(regs, a, b, c):
        regs[c] = regs[a] & regs[b]

    def bani(regs, a, b, c):
        regs[c] = regs[a] & b

    def borr(regs, a, b, c):
        regs[c] = regs[a] | regs[b]

    def bori(regs, a, b, c):
        regs[c] = regs[a] | b

    def setr(regs, a, b, c):
        regs[c] = regs[a]

    def seti(regs, a, b, c):
        regs[c] = a

    def gtir(regs, a, b, c):
        regs[c] = 1 if a > regs[b] else 0

    def gtri(regs, a, b, c):
        regs[c] = 1 if regs[a] > b else 0

    def gtrr(regs, a, b, c):
        regs[c] = 1 if regs[a] > regs[b] else 0

    def eqir(regs, a, b, c):
        regs[c] = 1 if a == regs[b] else 0

    def eqri(regs, a, b, c):
        regs[c] = 1 if regs[a] == b else 0

    def eqrr(regs, a, b, c):
        regs[c] = 1 if regs[a] == regs[b] else 0

    ops = {
        'addr': addr, 'addi': addi,
        'mulr': mulr, 'muli': muli,
        'banr': banr, 'bani': bani,
        'borr': borr, 'bori': bori,
        'setr': setr, 'seti': seti,
        'gtir': gtir, 'gtri': gtri, 'gtrr': gtrr,
        'eqir': eqir, 'eqri': eqri, 'eqrr': eqrr
    }

    lines = data.split('\n')
    ip_reg = int(lines[0].split()[1])

    instructions = []
    for line in lines[1:]:
        if line.strip():
            parts = line.split()
            op = parts[0]
            a, b, c = map(int, parts[1:4])
            instructions.append((op, a, b, c))

    regs = [0, 0, 0, 0, 0, 0]
    ip = 0

    while 0 <= ip < len(instructions):
        regs[ip_reg] = ip
        op, a, b, c = instructions[ip]
        ops[op](regs, a, b, c)
        ip = regs[ip_reg]
        ip += 1

    print(regs[0])
    AOC.submit_answer(regs[0])


if __name__ == "__main__":
    solve()
