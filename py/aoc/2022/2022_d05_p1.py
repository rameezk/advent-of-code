from aoc.helper import AOC


@AOC.puzzle(2022, 5, 1)
def solve():
    data = AOC.get_data()

#     data = """    [D]
# [N] [C]
# [Z] [M] [P]
#  1   2   3
#
# move 1 from 2 to 1
# move 3 from 1 to 3
# move 2 from 2 to 1
# move 1 from 1 to 2"""

    lines = data.split('\n')

    stack_lines = []
    move_lines = []
    is_move_section = False

    for line in lines:
        if line.strip() == '':
            is_move_section = True
            continue
        if is_move_section:
            move_lines.append(line)
        else:
            stack_lines.append(line)

    num_line = stack_lines[-1]
    stack_count = int(num_line.strip().split()[-1])

    stacks = [[] for _ in range(stack_count)]

    for line in reversed(stack_lines[:-1]):
        for i in range(stack_count):
            pos = 1 + i * 4
            if pos < len(line) and line[pos].strip():
                stacks[i].append(line[pos])

    for move in move_lines:
        parts = move.split()
        count = int(parts[1])
        from_stack = int(parts[3]) - 1
        to_stack = int(parts[5]) - 1

        for _ in range(count):
            if stacks[from_stack]:
                crate = stacks[from_stack].pop()
                stacks[to_stack].append(crate)

    result = ''.join(stack[-1] if stack else '' for stack in stacks)
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
