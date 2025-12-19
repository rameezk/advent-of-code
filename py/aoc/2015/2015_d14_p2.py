from aoc.helper import AOC


@AOC.puzzle(2015, 14, 2)
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
    num_reindeer = len(reindeer)

    distances = [0] * num_reindeer
    points = [0] * num_reindeer

    for second in range(1, race_time + 1):
        for i, (name, speed, fly_time, rest_time) in enumerate(reindeer):
            cycle_time = fly_time + rest_time
            time_in_cycle = (second - 1) % cycle_time

            if time_in_cycle < fly_time:
                distances[i] += speed

        max_distance = max(distances)
        for i in range(num_reindeer):
            if distances[i] == max_distance:
                points[i] += 1

    max_points = max(points)
    print(f"Max points: {max_points}")
    AOC.submit_answer(max_points)


if __name__ == "__main__":
    solve()
