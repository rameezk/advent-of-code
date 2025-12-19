from aoc.helper import AOC


@AOC.puzzle(2015, 14, 1)
def solve():
    sample_data = """Comet can fly 14 km/s for 10 seconds, but then must rest for 127 seconds.
Dancer can fly 16 km/s for 11 seconds, but then must rest for 162 seconds."""

    data = AOC.get_data().strip()

    lines = data.split('\n')
    reindeer = []

    for line in lines:
        parts = line.split()
        name = parts[0]
        speed = int(parts[3])
        fly_time = int(parts[6])
        rest_time = int(parts[13])
        reindeer.append((name, speed, fly_time, rest_time))

    race_time = 2503
    max_distance = 0

    for name, speed, fly_time, rest_time in reindeer:
        cycle_time = fly_time + rest_time
        full_cycles = race_time // cycle_time
        remaining_time = race_time % cycle_time

        distance = full_cycles * speed * fly_time
        distance += min(remaining_time, fly_time) * speed

        max_distance = max(max_distance, distance)

    print(f"Max distance: {max_distance}")
    AOC.submit_answer(max_distance)


if __name__ == "__main__":
    solve()
