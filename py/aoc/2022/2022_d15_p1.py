from aoc.helper import AOC


@AOC.puzzle(2022, 15, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """Sensor at x=2, y=18: closest beacon is at x=-2, y=15
# Sensor at x=9, y=16: closest beacon is at x=10, y=16
# Sensor at x=13, y=2: closest beacon is at x=15, y=3
# Sensor at x=12, y=14: closest beacon is at x=10, y=16
# Sensor at x=10, y=20: closest beacon is at x=10, y=16
# Sensor at x=14, y=17: closest beacon is at x=10, y=16
# Sensor at x=8, y=7: closest beacon is at x=2, y=10
# Sensor at x=2, y=0: closest beacon is at x=2, y=10
# Sensor at x=0, y=11: closest beacon is at x=2, y=10
# Sensor at x=20, y=14: closest beacon is at x=25, y=17
# Sensor at x=17, y=20: closest beacon is at x=21, y=22
# Sensor at x=16, y=7: closest beacon is at x=15, y=3
# Sensor at x=14, y=3: closest beacon is at x=15, y=3
# Sensor at x=20, y=1: closest beacon is at x=15, y=3"""

    target_y = 2000000

    sensors = []
    beacons = set()

    for line in data.strip().splitlines():
        parts = line.split()
        sx = int(parts[2][2:-1])
        sy = int(parts[3][2:-1])
        bx = int(parts[8][2:-1])
        by = int(parts[9][2:])

        distance = abs(sx - bx) + abs(sy - by)
        sensors.append((sx, sy, distance))
        beacons.add((bx, by))

    ranges = []
    for sx, sy, max_dist in sensors:
        dist_to_target = abs(sy - target_y)
        if dist_to_target <= max_dist:
            remaining = max_dist - dist_to_target
            ranges.append((sx - remaining, sx + remaining))

    ranges.sort()

    merged = []
    for start, end in ranges:
        if merged and start <= merged[-1][1] + 1:
            merged[-1] = (merged[-1][0], max(merged[-1][1], end))
        else:
            merged.append((start, end))

    total = sum(end - start + 1 for start, end in merged)

    beacons_on_target = len([b for b in beacons if b[1] == target_y])

    result = total - beacons_on_target
    print(result)


if __name__ == "__main__":
    solve()
