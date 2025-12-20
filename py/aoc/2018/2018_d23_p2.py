from aoc.helper import AOC
import heapq


@AOC.puzzle(2018, 23, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """pos=<10,12,12>, r=2
# pos=<12,14,12>, r=2
# pos=<16,12,12>, r=4
# pos=<14,14,14>, r=6
# pos=<50,50,50>, r=200
# pos=<10,10,10>, r=5""".strip().splitlines()

    nanobots = []
    for line in data:
        parts = line.split(", ")
        pos_str = parts[0].split("=")[1]
        x, y, z = map(int, pos_str[1:-1].split(","))
        r = int(parts[1].split("=")[1])
        nanobots.append((x, y, z, r))

    def manhattan(p1, p2):
        return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) + abs(p1[2] - p2[2])

    def count_in_range(pos):
        count = 0
        for nx, ny, nz, nr in nanobots:
            if manhattan(pos, (nx, ny, nz)) <= nr:
                count += 1
        return count

    min_x = min(n[0] for n in nanobots)
    max_x = max(n[0] for n in nanobots)
    min_y = min(n[1] for n in nanobots)
    max_y = max(n[1] for n in nanobots)
    min_z = min(n[2] for n in nanobots)
    max_z = max(n[2] for n in nanobots)

    size = max(max_x - min_x, max_y - min_y, max_z - min_z)
    step = 1
    while step < size:
        step *= 2

    heap = []

    def count_in_range_box(box_x, box_y, box_z, box_size):
        count = 0
        for nx, ny, nz, nr in nanobots:
            dist = 0
            if nx < box_x:
                dist += box_x - nx
            elif nx > box_x + box_size:
                dist += nx - (box_x + box_size)

            if ny < box_y:
                dist += box_y - ny
            elif ny > box_y + box_size:
                dist += ny - (box_y + box_size)

            if nz < box_z:
                dist += box_z - nz
            elif nz > box_z + box_size:
                dist += nz - (box_z + box_size)

            if dist <= nr:
                count += 1
        return count

    initial_count = count_in_range_box(min_x, min_y, min_z, step)
    dist_to_origin = abs(min_x) + abs(min_y) + abs(min_z)
    heapq.heappush(heap, (-initial_count, dist_to_origin, min_x, min_y, min_z, step))

    best_pos = None
    best_count = 0
    best_dist = float('inf')

    while heap:
        neg_count, dist, x, y, z, curr_step = heapq.heappop(heap)
        count = -neg_count

        if curr_step == 0:
            if count > best_count or (count == best_count and dist < best_dist):
                best_count = count
                best_dist = dist
                best_pos = (x, y, z)
            continue

        next_step = curr_step // 2
        for dx in [0, next_step]:
            for dy in [0, next_step]:
                for dz in [0, next_step]:
                    nx, ny, nz = x + dx, y + dy, z + dz
                    if next_step == 0:
                        box_count = count_in_range((nx, ny, nz))
                        box_dist = abs(nx) + abs(ny) + abs(nz)
                    else:
                        box_count = count_in_range_box(nx, ny, nz, next_step)
                        box_dist = abs(nx) + abs(ny) + abs(nz)

                    if box_count > best_count or (box_count == best_count and box_dist < best_dist):
                        heapq.heappush(heap, (-box_count, box_dist, nx, ny, nz, next_step))

    print(best_dist)
    AOC.submit_answer(best_dist)


if __name__ == "__main__":
    solve()
