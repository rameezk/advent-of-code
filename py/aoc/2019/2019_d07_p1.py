from aoc.helper import AOC
from itertools import permutations


def run_intcode(program, inputs):
    program = program.copy()
    pos = 0
    input_idx = 0
    outputs = []

    while True:
        instruction = program[pos]
        opcode = instruction % 100
        mode1 = (instruction // 100) % 10
        mode2 = (instruction // 1000) % 10

        if opcode == 99:
            break

        if opcode == 1:
            a = program[pos + 1] if mode1 == 1 else program[program[pos + 1]]
            b = program[pos + 2] if mode2 == 1 else program[program[pos + 2]]
            out_pos = program[pos + 3]
            program[out_pos] = a + b
            pos += 4
        elif opcode == 2:
            a = program[pos + 1] if mode1 == 1 else program[program[pos + 1]]
            b = program[pos + 2] if mode2 == 1 else program[program[pos + 2]]
            out_pos = program[pos + 3]
            program[out_pos] = a * b
            pos += 4
        elif opcode == 3:
            out_pos = program[pos + 1]
            program[out_pos] = inputs[input_idx]
            input_idx += 1
            pos += 2
        elif opcode == 4:
            a = program[pos + 1] if mode1 == 1 else program[program[pos + 1]]
            outputs.append(a)
            pos += 2
        elif opcode == 5:
            a = program[pos + 1] if mode1 == 1 else program[program[pos + 1]]
            b = program[pos + 2] if mode2 == 1 else program[program[pos + 2]]
            if a != 0:
                pos = b
            else:
                pos += 3
        elif opcode == 6:
            a = program[pos + 1] if mode1 == 1 else program[program[pos + 1]]
            b = program[pos + 2] if mode2 == 1 else program[program[pos + 2]]
            if a == 0:
                pos = b
            else:
                pos += 3
        elif opcode == 7:
            a = program[pos + 1] if mode1 == 1 else program[program[pos + 1]]
            b = program[pos + 2] if mode2 == 1 else program[program[pos + 2]]
            out_pos = program[pos + 3]
            program[out_pos] = 1 if a < b else 0
            pos += 4
        elif opcode == 8:
            a = program[pos + 1] if mode1 == 1 else program[program[pos + 1]]
            b = program[pos + 2] if mode2 == 1 else program[program[pos + 2]]
            out_pos = program[pos + 3]
            program[out_pos] = 1 if a == b else 0
            pos += 4

    return outputs[-1]


@AOC.puzzle(2019, 7, 1)
def solve():
    data = AOC.get_data().strip()

    program = list(map(int, data.split(',')))

    max_signal = 0
    for phase_sequence in permutations(range(5)):
        signal = 0
        for phase in phase_sequence:
            signal = run_intcode(program, [phase, signal])
        max_signal = max(max_signal, signal)

    answer = max_signal
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
