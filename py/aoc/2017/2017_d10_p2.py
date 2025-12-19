from aoc.helper import AOC
from functools import reduce

@AOC.puzzle(2017, 10, 2)
def solve():
    data = AOC.get_data().strip()

    lengths = [ord(c) for c in data]
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

    answer = ''.join(f'{byte:02x}' for byte in dense_hash)
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
