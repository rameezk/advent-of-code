from aoc.helper import AOC


@AOC.puzzle(2024, 25, 1)
def solve():
    data = AOC.get_data().strip()

    # data = """#####
# .####
# .####
# .####
# .#.#.
# .#...
# .....
#
# #####
# ##.##
# .#.##
# ...##
# ...#.
# ...#.
# .....
#
# .....
# #....
# #....
# #...#
# #.#.#
# #.###
# #####
#
# .....
# .....
# #.#..
# ###..
# ###.#
# ###.#
# #####
#
# .....
# .....
# .....
# #....
# #.#..
# #.#.#
# #####"""

    schematics = data.split("\n\n")

    locks = []
    keys = []

    for schematic in schematics:
        lines = schematic.strip().split("\n")

        is_lock = lines[0] == "#####"

        heights = []
        cols = len(lines[0])

        for col in range(cols):
            count = 0
            for row in range(1, len(lines) - 1):
                if lines[row][col] == "#":
                    count += 1
            heights.append(count)

        if is_lock:
            locks.append(heights)
        else:
            keys.append(heights)

    available_space = 5
    fit_count = 0

    for lock in locks:
        for key in keys:
            fits = True
            for i in range(len(lock)):
                if lock[i] + key[i] > available_space:
                    fits = False
                    break
            if fits:
                fit_count += 1

    print(fit_count)
    AOC.submit_answer(fit_count)


if __name__ == "__main__":
    solve()
