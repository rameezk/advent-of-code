from aoc.helper import AOC


@AOC.puzzle(2019, 2, 2)
def solve():
    data = AOC.get_data().strip()

    original_program = list(map(int, data.split(',')))

    target = 19690720

    for noun in range(100):
        for verb in range(100):
            program = original_program.copy()
            program[1] = noun
            program[2] = verb

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

            if program[0] == target:
                answer = 100 * noun + verb
                print(answer)
                AOC.submit_answer(answer)
                return


if __name__ == "__main__":
    solve()
