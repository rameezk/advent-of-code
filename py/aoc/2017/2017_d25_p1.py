from aoc.helper import AOC

@AOC.puzzle(2017, 25, 1)
def solve():
    data = AOC.get_data().strip()
    # data = """Begin in state A.
# Perform a diagnostic checksum after 6 steps.
#
# In state A:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state B.
#   If the current value is 1:
#     - Write the value 0.
#     - Move one slot to the left.
#     - Continue with state B.
#
# In state B:
#   If the current value is 0:
#     - Write the value 1.
#     - Move one slot to the left.
#     - Continue with state A.
#   If the current value is 1:
#     - Write the value 1.
#     - Move one slot to the right.
#     - Continue with state A."""

    lines = data.split('\n')

    start_state = lines[0].split()[-1].rstrip('.')
    steps = int(lines[1].split()[-2])

    states = {}
    i = 3
    while i < len(lines):
        if lines[i].startswith('In state'):
            state = lines[i].split()[-1].rstrip(':')

            val0_write = int(lines[i+2].split()[-1].rstrip('.'))
            val0_move = 1 if 'right' in lines[i+3] else -1
            val0_next = lines[i+4].split()[-1].rstrip('.')

            val1_write = int(lines[i+6].split()[-1].rstrip('.'))
            val1_move = 1 if 'right' in lines[i+7] else -1
            val1_next = lines[i+8].split()[-1].rstrip('.')

            states[state] = {
                0: (val0_write, val0_move, val0_next),
                1: (val1_write, val1_move, val1_next)
            }

            i += 9
        else:
            i += 1

    tape = {}
    cursor = 0
    current_state = start_state

    for _ in range(steps):
        current_value = tape.get(cursor, 0)
        write_value, move_dir, next_state = states[current_state][current_value]

        tape[cursor] = write_value
        cursor += move_dir
        current_state = next_state

    answer = sum(tape.values())
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
