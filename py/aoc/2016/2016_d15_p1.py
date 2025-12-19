from aoc.helper import AOC


@AOC.puzzle(2016, 15, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """Disc #1 has 5 positions; at time=0, it is at position 4.
# Disc #2 has 2 positions; at time=0, it is at position 1.""".splitlines()

    discs = []
    for line in data:
        parts = line.split()
        disc_num = int(parts[1][1:])
        num_positions = int(parts[3])
        initial_position = int(parts[-1][:-1])
        discs.append((disc_num, num_positions, initial_position))

    time = 0
    while True:
        all_aligned = True
        for disc_num, num_positions, initial_position in discs:
            position_at_capsule = (initial_position + time + disc_num) % num_positions
            if position_at_capsule != 0:
                all_aligned = False
                break

        if all_aligned:
            print(time)
            AOC.submit_answer(time)
            return

        time += 1


if __name__ == "__main__":
    solve()
