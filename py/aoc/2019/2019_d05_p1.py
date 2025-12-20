from aoc.helper import AOC


@AOC.puzzle(2019, 5, 1)
def solve():
    data = AOC.get_data().strip()

    program = list(map(int, data.split(',')))

    pos = 0
    outputs = []

    while True:
        instruction = program[pos]
        opcode = instruction % 100
        mode1 = (instruction // 100) % 10
        mode2 = (instruction // 1000) % 10
        mode3 = (instruction // 10000) % 10

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
            program[out_pos] = 1
            pos += 2
        elif opcode == 4:
            a = program[pos + 1] if mode1 == 1 else program[program[pos + 1]]
            outputs.append(a)
            pos += 2

    answer = outputs[-1]
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
