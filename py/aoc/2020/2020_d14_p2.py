from aoc.helper import AOC
from itertools import product

@AOC.puzzle(2020, 14, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """mask = 000000000000000000000000000000X1001X
# mem[42] = 100
# mask = 00000000000000000000000000000000X0XX
# mem[26] = 1""".splitlines()

    memory = {}
    mask = ""

    for line in data:
        if line.startswith("mask"):
            mask = line.split(" = ")[1]
        else:
            parts = line.split(" = ")
            addr = int(parts[0][4:-1])
            value = int(parts[1])

            addr_bin = bin(addr)[2:].zfill(36)

            masked_addr = []
            for i, bit in enumerate(mask):
                if bit == '0':
                    masked_addr.append(addr_bin[i])
                elif bit == '1':
                    masked_addr.append('1')
                else:
                    masked_addr.append('X')

            x_count = masked_addr.count('X')
            for combo in product(['0', '1'], repeat=x_count):
                result = masked_addr[:]
                combo_idx = 0
                for i in range(len(result)):
                    if result[i] == 'X':
                        result[i] = combo[combo_idx]
                        combo_idx += 1
                final_addr = int(''.join(result), 2)
                memory[final_addr] = value

    answer = sum(memory.values())

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
