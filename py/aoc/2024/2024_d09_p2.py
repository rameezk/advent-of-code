from itertools import batched

from aoc.helper import AOC
from aoc.util import benchmark


def find_leftmost_free_space_position(disk: list, needed_size: int) -> int:
    count, start = 0, 0

    for i, val in enumerate(disk):
        if val == ".":
            if count == 0:
                start = i
            count += 1
            if count >= needed_size:
                return start
        else:
            count = 0

    return -1


@benchmark
@AOC.puzzle(year=2024, day=9, part=2)
def solve():
    data = "2333133121414131402"
    data = AOC.get_data().strip()

    disk: list = []

    file_positions = {}
    cursor_position = 0

    largest_file_id = -1
    for id_, batch in enumerate(batched(data, 2)):
        block_size = int(batch[0])
        free_space = int(batch[1]) if len(batch) > 1 else 0

        disk.extend([id_] * block_size)
        disk.extend(["."] * free_space)

        file_positions[id_] = list(range(cursor_position, cursor_position + block_size))
        cursor_position += block_size + free_space

        largest_file_id = id_

    for file_id in range(largest_file_id, -1, -1):
        if file_id not in file_positions:
            continue

        file_blocks = file_positions[file_id]

        file_start = file_blocks[0]
        file_size = len(file_blocks)

        free_space_position = find_leftmost_free_space_position(
            disk[:file_start], file_size
        )
        if free_space_position != -1:
            content = [disk[i] for i in file_blocks]
            for i in file_blocks:
                disk[i] = "."
            for i in range(file_size):
                disk[free_space_position + i] = content[i]

    checksum = 0
    for cursor_position, id_ in enumerate(disk):
        if id_ != ".":
            checksum += cursor_position * int(id_)

    print(checksum)
    AOC.submit_answer(checksum)


if __name__ == "__main__":
    solve()
