from itertools import batched

from aoc.helper import AOC


@AOC.puzzle(year=2024, day=9, part=1)
def solve():
    data = "2333133121414131402"
    data = AOC.get_data().strip()

    disk: list = []
    for id_, batch in enumerate(batched(data, 2)):
        block_size = int(batch[0])
        free_space = int(batch[1]) if len(batch) > 1 else 0
        disk.extend([id_] * block_size)
        disk.extend(["."] * free_space)

    while True:
        try:
            left_space = disk.index(".")
        except ValueError:
            break

        while len(disk) and disk[-1] == ".":
            disk.pop()

        if left_space < len(disk):
            disk[left_space] = disk.pop()

    checksum = 0
    for pos, id_ in enumerate(disk):
        checksum += pos * int(id_)

    print(checksum)
    AOC.submit_answer(checksum)


if __name__ == "__main__":
    solve()
