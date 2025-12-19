from aoc.helper import AOC
from functools import reduce

def knot_hash(input_string):
    lengths = [ord(c) for c in input_string]
    lengths.extend([17, 31, 73, 47, 23])

    list_size = 256
    numbers = list(range(list_size))
    current_pos = 0
    skip_size = 0

    for _ in range(64):
        for length in lengths:
            indices = [(current_pos + i) % list_size for i in range(length)]
            values = [numbers[idx] for idx in indices]
            values.reverse()
            for i, idx in enumerate(indices):
                numbers[idx] = values[i]

            current_pos = (current_pos + length + skip_size) % list_size
            skip_size += 1

    dense_hash = []
    for block_idx in range(16):
        block = numbers[block_idx * 16:(block_idx + 1) * 16]
        xor_result = reduce(lambda a, b: a ^ b, block)
        dense_hash.append(xor_result)

    return ''.join(f'{byte:02x}' for byte in dense_hash)

@AOC.puzzle(2017, 14, 1)
def solve():
    data = AOC.get_data().strip()
    # data = """flqrgnkx"""

    used_count = 0
    for row in range(128):
        hash_input = f"{data}-{row}"
        hash_hex = knot_hash(hash_input)

        for hex_char in hash_hex:
            binary = bin(int(hex_char, 16))[2:].zfill(4)
            used_count += binary.count('1')

    answer = used_count
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
