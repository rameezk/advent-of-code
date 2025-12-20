from aoc.helper import AOC

@AOC.puzzle(2020, 8, 2)
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

    def run_program(instructions):
        accumulator = 0
        pc = 0
        visited = set()

        while pc < len(instructions):
            if pc in visited:
                return None

            visited.add(pc)
            op, arg = instructions[pc]

            if op == "acc":
                accumulator += arg
                pc += 1
            elif op == "jmp":
                pc += arg
            else:
                pc += 1

        return accumulator

    for i in range(len(instructions)):
        op, arg = instructions[i]

        if op == "acc":
            continue

        modified_instructions = instructions[:]
        if op == "jmp":
            modified_instructions[i] = ("nop", arg)
        else:
            modified_instructions[i] = ("jmp", arg)

        result = run_program(modified_instructions)
        if result is not None:
            answer = result
            break

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
