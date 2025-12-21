from aoc.helper import AOC


@AOC.puzzle(2022, 17, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """>>><<><>><<<>><>>><<<>>><<<><<<>><>><<>>"""

    rocks = [
        [(0, 0), (1, 0), (2, 0), (3, 0)],
        [(1, 0), (0, 1), (1, 1), (2, 1), (1, 2)],
        [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)],
        [(0, 0), (0, 1), (0, 2), (0, 3)],
        [(0, 0), (1, 0), (0, 1), (1, 1)]
    ]

    chamber = set()
    jet_index = 0
    max_height = 0

    for rock_num in range(2022):
        rock = rocks[rock_num % 5]
        x, y = 2, max_height + 3

        while True:
            jet = data[jet_index % len(data)]
            jet_index += 1

            dx = 1 if jet == '>' else -1
            new_positions = [(x + dx + rx, y + ry) for rx, ry in rock]

            if all(0 <= nx < 7 and (nx, ny) not in chamber for nx, ny in new_positions):
                x += dx

            new_positions = [(x + rx, y + ry - 1) for rx, ry in rock]

            if any(ny < 0 or (nx, ny) in chamber for nx, ny in new_positions):
                for rx, ry in rock:
                    chamber.add((x + rx, y + ry))
                    max_height = max(max_height, y + ry + 1)
                break

            y -= 1

    print(max_height)
    AOC.submit_answer(max_height)


if __name__ == "__main__":
    solve()
