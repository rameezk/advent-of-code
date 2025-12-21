from aoc.helper import AOC


@AOC.puzzle(2022, 17, 2)
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
    total_rocks = 1000000000000

    seen_states = {}
    heights_at_rock = []

    rock_num = 0
    while rock_num < total_rocks:
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

        heights_at_rock.append(max_height)

        top_rows = []
        for dy in range(min(30, max_height)):
            row = tuple(1 if (cx, max_height - 1 - dy) in chamber else 0 for cx in range(7))
            top_rows.append(row)

        state = (rock_num % 5, jet_index % len(data), tuple(top_rows))

        if state in seen_states:
            prev_rock_num, prev_height = seen_states[state]
            cycle_length = rock_num - prev_rock_num
            cycle_height = max_height - prev_height

            remaining_rocks = total_rocks - rock_num
            full_cycles = remaining_rocks // cycle_length
            leftover_rocks = remaining_rocks % cycle_length

            final_height = max_height + full_cycles * cycle_height

            if leftover_rocks > 0:
                final_height += heights_at_rock[prev_rock_num + leftover_rocks - 1] - prev_height

            print(final_height)
            AOC.submit_answer(final_height)
            return

        seen_states[state] = (rock_num, max_height)
        rock_num += 1

    print(max_height)
    AOC.submit_answer(max_height)


if __name__ == "__main__":
    solve()
