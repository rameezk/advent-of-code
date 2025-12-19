from aoc.helper import AOC
from collections import deque

@AOC.puzzle(2017, 18, 2)
def solve():
    data = AOC.get_data().strip()
    # data = """snd 1
# snd 2
# snd p
# rcv a
# rcv b
# rcv c
# rcv d"""

    instructions = [line.split() for line in data.split('\n')]

    class Program:
        def __init__(self, pid, instructions):
            self.pid = pid
            self.instructions = instructions
            self.registers = {'p': pid}
            self.pc = 0
            self.queue = deque()
            self.send_count = 0
            self.waiting = False

        def get_value(self, x):
            try:
                return int(x)
            except ValueError:
                return self.registers.get(x, 0)

        def step(self, other):
            if self.pc < 0 or self.pc >= len(self.instructions):
                return False

            inst = self.instructions[self.pc]
            op = inst[0]

            if op == 'snd':
                value = self.get_value(inst[1])
                other.queue.append(value)
                self.send_count += 1
                self.pc += 1
                self.waiting = False
            elif op == 'set':
                self.registers[inst[1]] = self.get_value(inst[2])
                self.pc += 1
                self.waiting = False
            elif op == 'add':
                self.registers[inst[1]] = self.registers.get(inst[1], 0) + self.get_value(inst[2])
                self.pc += 1
                self.waiting = False
            elif op == 'mul':
                self.registers[inst[1]] = self.registers.get(inst[1], 0) * self.get_value(inst[2])
                self.pc += 1
                self.waiting = False
            elif op == 'mod':
                self.registers[inst[1]] = self.registers.get(inst[1], 0) % self.get_value(inst[2])
                self.pc += 1
                self.waiting = False
            elif op == 'rcv':
                if self.queue:
                    self.registers[inst[1]] = self.queue.popleft()
                    self.pc += 1
                    self.waiting = False
                else:
                    self.waiting = True
                    return True
            elif op == 'jgz':
                if self.get_value(inst[1]) > 0:
                    self.pc += self.get_value(inst[2])
                else:
                    self.pc += 1
                self.waiting = False

            return True

    prog0 = Program(0, instructions)
    prog1 = Program(1, instructions)

    while True:
        active0 = prog0.step(prog1)
        active1 = prog1.step(prog0)

        if not active0 and not active1:
            break

        if prog0.waiting and prog1.waiting and not prog0.queue and not prog1.queue:
            break

    answer = prog1.send_count
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
