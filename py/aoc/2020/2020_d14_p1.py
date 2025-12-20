from aoc.helper import AOC

@AOC.puzzle(2020, 14, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
# mem[8] = 11
# mem[7] = 101
# mem[8] = 0""".splitlines()

    memory = {}
    mask = ""

    for line in data:
        if line.startswith("mask"):
            mask = line.split(" = ")[1]
        else:
            parts = line.split(" = ")
            addr = int(parts[0][4:-1])
            value = int(parts[1])

            value_bin = bin(value)[2:].zfill(36)

            result = []
            for i, bit in enumerate(mask):
                if bit == 'X':
                    result.append(value_bin[i])
                else:
                    result.append(bit)

            memory[addr] = int(''.join(result), 2)

    answer = sum(memory.values())

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
