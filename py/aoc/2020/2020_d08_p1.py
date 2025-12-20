from aoc.helper import AOC

@AOC.puzzle(2020, 8, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """nop +0
# acc +1
# jmp +4
# acc +3
# jmp -3
# acc -99
# acc +1
# jmp -4
# acc +6""".splitlines()

    instructions = []
    for line in data:
        op, arg = line.split()
        instructions.append((op, int(arg)))

    accumulator = 0
    pc = 0
    visited = set()

    while pc < len(instructions):
        if pc in visited:
            break

        visited.add(pc)
        op, arg = instructions[pc]

        if op == "acc":
            accumulator += arg
            pc += 1
        elif op == "jmp":
            pc += arg
        else:
            pc += 1

    answer = accumulator
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
