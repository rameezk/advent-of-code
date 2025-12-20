from aoc.helper import AOC
from collections import deque


class IntcodeComputer:
    def __init__(self, program, address):
        self.memory = {i: val for i, val in enumerate(program)}
        self.pos = 0
        self.relative_base = 0
        self.halted = False
        self.address = address
        self.input_queue = deque([address])
        self.output_buffer = []

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

    def add_input(self, value):
        self.input_queue.append(value)

    def step(self):
        instruction = self.memory.get(self.pos, 0)
        opcode = instruction % 100
        mode1 = (instruction // 100) % 10
        mode2 = (instruction // 1000) % 10
        mode3 = (instruction // 10000) % 10

        if opcode == 99:
            self.halted = True
            return None

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
            out_pos = self.get_addr(1, mode1)
            if len(self.input_queue) > 0:
                self.memory[out_pos] = self.input_queue.popleft()
            else:
                self.memory[out_pos] = -1
            self.pos += 2
        elif opcode == 4:
            a = self.get_value(1, mode1)
            self.output_buffer.append(a)
            self.pos += 2
            if len(self.output_buffer) == 3:
                packet = self.output_buffer[:]
                self.output_buffer = []
                return packet
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

        return None


@AOC.puzzle(2019, 23, 1)
def solve():
    data = AOC.get_data().strip()

    program = list(map(int, data.split(',')))

    computers = [IntcodeComputer(program[:], i) for i in range(50)]

    while True:
        for computer in computers:
            if computer.halted:
                continue

            packet = computer.step()

            if packet is not None:
                dest, x, y = packet
                if dest == 255:
                    answer = y
                    print(answer)
                    AOC.submit_answer(answer)
                    return
                elif 0 <= dest < 50:
                    computers[dest].add_input(x)
                    computers[dest].add_input(y)


if __name__ == "__main__":
    solve()
