from aoc.helper import AOC


@AOC.puzzle(2025, 9, 2)
def solve():
    data = AOC.get_data()

    red_tiles = []
    for line in data.strip().splitlines():
        x, y = map(int, line.split(','))
        red_tiles.append((x, y))

    edges = build_edges(red_tiles)
    boundary = set(red_tiles) | build_border_tiles(red_tiles)

    areas = []
    for i in range(len(red_tiles)):
        for j in range(i + 1, len(red_tiles)):
            c1 = red_tiles[i]
            c2 = red_tiles[j]
            if is_valid_rectangle(c1, c2, edges, boundary):
                areas.append(area(c1, c2))

    result = max(areas)
    print(result)
    AOC.submit_answer(result)


def area(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    return (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)


def build_edges(red_tiles):
    edges = []
    n = len(red_tiles)
    for i in range(n):
        edges.append((red_tiles[i], red_tiles[(i + 1) % n]))
    return edges


def build_border_tiles(red_tiles):
    border = set()
    n = len(red_tiles)
    for i in range(n):
        c1, c2 = red_tiles[i], red_tiles[(i + 1) % n]
        border.update(line_between(c1, c2))
    return border


def line_between(c1, c2):
    x1, y1 = c1
    x2, y2 = c2
    if x1 == x2:
        return {(x1, y) for y in range(min(y1, y2) + 1, max(y1, y2))}
    else:
        return {(x, y1) for x in range(min(x1, x2) + 1, max(x1, x2))}


def point_in_polygon(x, y, edges):
    crossings = 0
    for (x1, y1), (x2, y2) in edges:
        if y1 == y2:
            continue
        if y < min(y1, y2) or y >= max(y1, y2):
            continue
        x_intersect = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
        if x < x_intersect:
            crossings += 1
    return crossings % 2 == 1


def is_valid_rectangle(c1, c2, edges, boundary):
    x1, y1 = c1
    x2, y2 = c2
    min_x, max_x = min(x1, x2), max(x1, x2)
    min_y, max_y = min(y1, y2), max(y1, y2)

    corners = [(min_x, min_y), (min_x, max_y), (max_x, min_y), (max_x, max_y)]
    for cx, cy in corners:
        if (cx, cy) not in boundary and not point_in_polygon(cx, cy, edges):
            return False

    for (ex1, ey1), (ex2, ey2) in edges:
        if edge_crosses_interior(ex1, ey1, ex2, ey2, min_x, max_x, min_y, max_y):
            return False

    return True


def edge_crosses_interior(ex1, ey1, ex2, ey2, min_x, max_x, min_y, max_y):
    if ex1 == ex2:
        in_x = min_x < ex1 < max_x
        overlaps_y = min(ey1, ey2) < max_y and max(ey1, ey2) > min_y
        return in_x and overlaps_y
    else:
        in_y = min_y < ey1 < max_y
        overlaps_x = min(ex1, ex2) < max_x and max(ex1, ex2) > min_x
        return in_y and overlaps_x


if __name__ == "__main__":
    solve()
