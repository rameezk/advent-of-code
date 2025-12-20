from aoc.helper import AOC
from itertools import permutations


class IntcodeComputer:
    def __init__(self, program):
        self.program = program.copy()
        self.pos = 0
        self.halted = False

    def run(self, inputs):
        input_idx = 0
        outputs = []

        while True:
            instruction = self.program[self.pos]
            opcode = instruction % 100
            mode1 = (instruction // 100) % 10
            mode2 = (instruction // 1000) % 10

            if opcode == 99:
                self.halted = True
                return outputs

            if opcode == 1:
                a = self.program[self.pos + 1] if mode1 == 1 else self.program[self.program[self.pos + 1]]
                b = self.program[self.pos + 2] if mode2 == 1 else self.program[self.program[self.pos + 2]]
                out_pos = self.program[self.pos + 3]
                self.program[out_pos] = a + b
                self.pos += 4
            elif opcode == 2:
                a = self.program[self.pos + 1] if mode1 == 1 else self.program[self.program[self.pos + 1]]
                b = self.program[self.pos + 2] if mode2 == 1 else self.program[self.program[self.pos + 2]]
                out_pos = self.program[self.pos + 3]
                self.program[out_pos] = a * b
                self.pos += 4
            elif opcode == 3:
                if input_idx >= len(inputs):
                    return outputs
                out_pos = self.program[self.pos + 1]
                self.program[out_pos] = inputs[input_idx]
                input_idx += 1
                self.pos += 2
            elif opcode == 4:
                a = self.program[self.pos + 1] if mode1 == 1 else self.program[self.program[self.pos + 1]]
                outputs.append(a)
                self.pos += 2
            elif opcode == 5:
                a = self.program[self.pos + 1] if mode1 == 1 else self.program[self.program[self.pos + 1]]
                b = self.program[self.pos + 2] if mode2 == 1 else self.program[self.program[self.pos + 2]]
                if a != 0:
                    self.pos = b
                else:
                    self.pos += 3
            elif opcode == 6:
                a = self.program[self.pos + 1] if mode1 == 1 else self.program[self.program[self.pos + 1]]
                b = self.program[self.pos + 2] if mode2 == 1 else self.program[self.program[self.pos + 2]]
                if a == 0:
                    self.pos = b
                else:
                    self.pos += 3
            elif opcode == 7:
                a = self.program[self.pos + 1] if mode1 == 1 else self.program[self.program[self.pos + 1]]
                b = self.program[self.pos + 2] if mode2 == 1 else self.program[self.program[self.pos + 2]]
                out_pos = self.program[self.pos + 3]
                self.program[out_pos] = 1 if a < b else 0
                self.pos += 4
            elif opcode == 8:
                a = self.program[self.pos + 1] if mode1 == 1 else self.program[self.program[self.pos + 1]]
                b = self.program[self.pos + 2] if mode2 == 1 else self.program[self.program[self.pos + 2]]
                out_pos = self.program[self.pos + 3]
                self.program[out_pos] = 1 if a == b else 0
                self.pos += 4


@AOC.puzzle(2019, 7, 2)
def solve():
    data = AOC.get_data().strip()

    program = list(map(int, data.split(',')))

    max_signal = 0
    for phase_sequence in permutations(range(5, 10)):
        amplifiers = [IntcodeComputer(program) for _ in range(5)]

        for i, phase in enumerate(phase_sequence):
            amplifiers[i].run([phase])

        signal = 0
        while not amplifiers[4].halted:
            for amp in amplifiers:
                outputs = amp.run([signal])
                if outputs:
                    signal = outputs[-1]

        max_signal = max(max_signal, signal)

    answer = max_signal
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
