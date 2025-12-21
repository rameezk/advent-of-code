from aoc.helper import AOC


@AOC.puzzle(2022, 15, 2)
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

    max_coord = 4000000

    sensors = []
    for line in data.strip().splitlines():
        parts = line.split()
        sx = int(parts[2][2:-1])
        sy = int(parts[3][2:-1])
        bx = int(parts[8][2:-1])
        by = int(parts[9][2:])

        distance = abs(sx - bx) + abs(sy - by)
        sensors.append((sx, sy, distance))

    def get_ranges_for_row(y):
        ranges = []
        for sx, sy, max_dist in sensors:
            dist_to_target = abs(sy - y)
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

        return merged

    for y in range(max_coord + 1):
        ranges = get_ranges_for_row(y)

        clipped_ranges = []
        for start, end in ranges:
            clipped_start = max(start, 0)
            clipped_end = min(end, max_coord)
            if clipped_start <= clipped_end:
                clipped_ranges.append((clipped_start, clipped_end))

        if not clipped_ranges:
            continue

        if len(clipped_ranges) > 1:
            x = clipped_ranges[0][1] + 1
            result = x * 4000000 + y
            print(result)
            break

        if clipped_ranges[0][0] > 0:
            x = 0
            result = x * 4000000 + y
            print(result)
            break

        if clipped_ranges[0][1] < max_coord:
            x = max_coord
            result = x * 4000000 + y
            print(result)
            break


if __name__ == "__main__":
    solve()
