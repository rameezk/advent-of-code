from aoc.helper import AOC


@AOC.puzzle(2019, 2, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """1,9,10,3,2,3,11,0,99,30,40,50"""

    program = list(map(int, data.split(',')))

    program[1] = 12
    program[2] = 2

    pos = 0
    while True:
        opcode = program[pos]

        if opcode == 99:
            break

        a_pos = program[pos + 1]
        b_pos = program[pos + 2]
        out_pos = program[pos + 3]

        if opcode == 1:
            program[out_pos] = program[a_pos] + program[b_pos]
        elif opcode == 2:
            program[out_pos] = program[a_pos] * program[b_pos]

        pos += 4

    answer = program[0]
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
