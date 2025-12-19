from aoc.helper import AOC
from functools import reduce
from collections import deque

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

def build_grid(key):
    grid = []
    for row in range(128):
        hash_input = f"{key}-{row}"
        hash_hex = knot_hash(hash_input)

        row_bits = ""
        for hex_char in hash_hex:
            binary = bin(int(hex_char, 16))[2:].zfill(4)
            row_bits += binary

        grid.append(row_bits)
    return grid

def count_regions(grid):
    visited = set()
    regions = 0

    def bfs(start_r, start_c):
        queue = deque([(start_r, start_c)])
        visited.add((start_r, start_c))

        while queue:
            r, c = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < 128 and 0 <= nc < 128:
                    if (nr, nc) not in visited and grid[nr][nc] == '1':
                        visited.add((nr, nc))
                        queue.append((nr, nc))

    for r in range(128):
        for c in range(128):
            if grid[r][c] == '1' and (r, c) not in visited:
                bfs(r, c)
                regions += 1

    return regions

@AOC.puzzle(2017, 14, 2)
def solve():
    data = AOC.get_data().strip()
    # data = """flqrgnkx"""

    grid = build_grid(data)
    answer = count_regions(grid)
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
