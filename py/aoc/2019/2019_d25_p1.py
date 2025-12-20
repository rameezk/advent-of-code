from aoc.helper import AOC
from itertools import combinations


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


def send_command(computer, command):
    ascii_input = [ord(c) for c in command] + [10]
    return computer.run(ascii_input)


def output_to_text(outputs):
    return ''.join(chr(c) for c in outputs if c < 256)


@AOC.puzzle(2019, 25, 1)
def solve():
    data = AOC.get_data().strip()
    program = list(map(int, data.split(',')))

    item_paths = {
        "fuel cell": ["south"],
        "mouse": ["west"],
        "planetoid": ["north", "west", "south"],
        "klein bottle": ["west", "north", "east"],
        "dark matter": ["west", "west", "south"],
        "mutex": ["north", "west", "south", "east"],
        "antenna": ["north", "west", "south", "west"],
        "whirled peas": ["north", "west", "south", "east", "south"]
    }

    checkpoint_path = ["north", "west", "south", "east", "south", "south", "east"]

    computer = IntcodeComputer(program)
    output = computer.run([])

    opposite = {"north": "south", "south": "north", "east": "west", "west": "east"}

    for item, path in item_paths.items():
        for direction in path:
            send_command(computer, direction)
        send_command(computer, f"take {item}")
        for direction in reversed(path):
            send_command(computer, opposite[direction])

    for direction in checkpoint_path:
        send_command(computer, direction)

    items = list(item_paths.keys())

    for item in items:
        send_command(computer, f"drop {item}")

    for r in range(1, len(items) + 1):
        for combo in combinations(items, r):
            for item in combo:
                send_command(computer, f"take {item}")

            output = send_command(computer, "north")
            text = output_to_text(output)

            if "lighter" not in text and "heavier" not in text:
                for line in text.split('\n'):
                    if 'typing' in line:
                        parts = line.split()
                        for i, part in enumerate(parts):
                            if part == 'typing' and i + 1 < len(parts):
                                answer = parts[i + 1].strip('.')
                                print(answer)
                                AOC.submit_answer(answer)
                                return

            for item in combo:
                send_command(computer, f"drop {item}")


if __name__ == "__main__":
    solve()
