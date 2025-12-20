from aoc.helper import AOC


class IntcodeComputer:
    def __init__(self, program):
        self.memory = {i: val for i, val in enumerate(program)}
        self.pos = 0
        self.relative_base = 0
        self.halted = False

    def get_value(self, offset, mode):
        param = self.memory.get(self.pos + offset, 0)
        if mode == 0:
            return self.memory.get(param, 0)
        elif mode == 1:
            return param
        elif mode == 2:
            return self.memory.get(self.relative_base + param, 0)

    def get_addr(self, offset, mode):
        param = self.memory.get(self.pos + offset, 0)
        if mode == 0:
            return param
        elif mode == 2:
            return self.relative_base + param

    def run(self, inputs):
        input_idx = 0
        outputs = []

        while True:
            instruction = self.memory.get(self.pos, 0)
            opcode = instruction % 100
            mode1 = (instruction // 100) % 10
            mode2 = (instruction // 1000) % 10
            mode3 = (instruction // 10000) % 10

            if opcode == 99:
                self.halted = True
                return outputs

            if opcode == 1:
                a = self.get_value(1, mode1)
                b = self.get_value(2, mode2)
                out_pos = self.get_addr(3, mode3)
                self.memory[out_pos] = a + b
                self.pos += 4
            elif opcode == 2:
                a = self.get_value(1, mode1)
                b = self.get_value(2, mode2)
                out_pos = self.get_addr(3, mode3)
                self.memory[out_pos] = a * b
                self.pos += 4
            elif opcode == 3:
                if input_idx >= len(inputs):
                    return outputs
                out_pos = self.get_addr(1, mode1)
                self.memory[out_pos] = inputs[input_idx]
                input_idx += 1
                self.pos += 2
            elif opcode == 4:
                a = self.get_value(1, mode1)
                outputs.append(a)
                self.pos += 2
            elif opcode == 5:
                a = self.get_value(1, mode1)
                b = self.get_value(2, mode2)
                if a != 0:
                    self.pos = b
                else:
                    self.pos += 3
            elif opcode == 6:
                a = self.get_value(1, mode1)
                b = self.get_value(2, mode2)
                if a == 0:
                    self.pos = b
                else:
                    self.pos += 3
            elif opcode == 7:
                a = self.get_value(1, mode1)
                b = self.get_value(2, mode2)
                out_pos = self.get_addr(3, mode3)
                self.memory[out_pos] = 1 if a < b else 0
                self.pos += 4
            elif opcode == 8:
                a = self.get_value(1, mode1)
                b = self.get_value(2, mode2)
                out_pos = self.get_addr(3, mode3)
                self.memory[out_pos] = 1 if a == b else 0
                self.pos += 4
            elif opcode == 9:
                a = self.get_value(1, mode1)
                self.relative_base += a
                self.pos += 2


@AOC.puzzle(2019, 13, 2)
def solve():
    data = AOC.get_data().strip()

    program = list(map(int, data.split(',')))
    program[0] = 2

    computer = IntcodeComputer(program)

    score = 0
    ball_x = 0
    paddle_x = 0

    while not computer.halted:
        if ball_x < paddle_x:
            joystick = -1
        elif ball_x > paddle_x:
            joystick = 1
        else:
            joystick = 0

        outputs = computer.run([joystick])

        if len(outputs) == 0:
            break

        for i in range(0, len(outputs), 3):
            x = outputs[i]
            y = outputs[i + 1]
            tile_id = outputs[i + 2]

            if x == -1 and y == 0:
                score = tile_id
            elif tile_id == 3:
                paddle_x = x
            elif tile_id == 4:
                ball_x = x

    answer = score
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
