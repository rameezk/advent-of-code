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


@AOC.puzzle(2019, 17, 2)
def solve():
    data = AOC.get_data().strip()

    program = list(map(int, data.split(',')))

    computer = IntcodeComputer(program)
    output = computer.run([])

    grid = []
    row = []
    robot_pos = None
    robot_dir = None

    y = 0
    for val in output:
        if val == 10:
            if row:
                grid.append(row)
                row = []
                y += 1
        else:
            char = chr(val)
            if char in '^v<>':
                robot_pos = (len(row), len(grid))
                robot_dir = char
            row.append(char)

    dirs = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}
    left_turn = {'^': '<', '<': 'v', 'v': '>', '>': '^'}
    right_turn = {'^': '>', '>': 'v', 'v': '<', '<': '^'}

    x, y = robot_pos
    d = robot_dir
    path = []

    while True:
        dx, dy = dirs[d]
        steps = 0
        while True:
            nx, ny = x + dx, y + dy
            if 0 <= ny < len(grid) and 0 <= nx < len(grid[ny]) and grid[ny][nx] == '#':
                x, y = nx, ny
                steps += 1
            else:
                break

        if steps > 0:
            path.append(str(steps))

        left_d = left_turn[d]
        ldx, ldy = dirs[left_d]
        lnx, lny = x + ldx, y + ldy

        right_d = right_turn[d]
        rdx, rdy = dirs[right_d]
        rnx, rny = x + rdx, y + rdy

        if 0 <= lny < len(grid) and 0 <= lnx < len(grid[lny]) and grid[lny][lnx] == '#':
            path.append('L')
            d = left_d
        elif 0 <= rny < len(grid) and 0 <= rnx < len(grid[rny]) and grid[rny][rnx] == '#':
            path.append('R')
            d = right_d
        else:
            break

    full_path = ','.join(path)

    A = "R,6,L,10,R,8"
    B = "R,8,R,12,L,8,L,8"
    C = "L,10,R,6,R,6,L,8"

    main = "A,B,A,B,C,A,B,C,A,C"

    main_input = [ord(c) for c in main] + [10]
    a_input = [ord(c) for c in A] + [10]
    b_input = [ord(c) for c in B] + [10]
    c_input = [ord(c) for c in C] + [10]
    video_input = [ord('n'), 10]

    program[0] = 2
    computer = IntcodeComputer(program)
    all_inputs = main_input + a_input + b_input + c_input + video_input
    output = computer.run(all_inputs)

    answer = output[-1]
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
