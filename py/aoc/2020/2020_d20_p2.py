from aoc.helper import AOC
import math

@AOC.puzzle(2020, 20, 2)
def solve():
    data = AOC.get_data().strip()

    tiles = {}
    for tile_block in data.split("\n\n"):
        lines = tile_block.strip().split("\n")
        tile_id = int(lines[0].split()[1].rstrip(":"))
        grid = [list(line) for line in lines[1:]]
        tiles[tile_id] = grid

    def rotate_90(grid):
        n = len(grid)
        return [[grid[n-1-j][i] for j in range(n)] for i in range(n)]

    def flip_h(grid):
        return [row[::-1] for row in grid]

    def get_borders(grid):
        top = "".join(grid[0])
        bottom = "".join(grid[-1])
        left = "".join(row[0] for row in grid)
        right = "".join(row[-1] for row in grid)
        return {"top": top, "right": right, "bottom": bottom, "left": left}

    def all_orientations(grid):
        orientations = []
        current = grid
        for _ in range(4):
            orientations.append(current)
            orientations.append(flip_h(current))
            current = rotate_90(current)
        return orientations

    def find_neighbors(tiles):
        tile_neighbors = {}
        for tid1, grid1 in tiles.items():
            neighbors = {}
            for tid2, grid2 in tiles.items():
                if tid1 == tid2:
                    continue
                for orient in all_orientations(grid2):
                    b1 = get_borders(grid1)
                    b2 = get_borders(orient)
                    if b1["right"] == b2["left"]:
                        neighbors["right"] = (tid2, orient)
                    if b1["bottom"] == b2["top"]:
                        neighbors["bottom"] = (tid2, orient)
                    if b1["left"] == b2["right"]:
                        neighbors["left"] = (tid2, orient)
                    if b1["top"] == b2["bottom"]:
                        neighbors["top"] = (tid2, orient)
            tile_neighbors[tid1] = neighbors
        return tile_neighbors

    tile_neighbors = {}
    for tile_id, grid in tiles.items():
        for orient in all_orientations(grid):
            neighbors = set()
            b1 = get_borders(orient)
            for tid2, grid2 in tiles.items():
                if tile_id == tid2:
                    continue
                for orient2 in all_orientations(grid2):
                    b2 = get_borders(orient2)
                    if b1["top"] == b2["bottom"] or b1["bottom"] == b2["top"] or \
                       b1["left"] == b2["right"] or b1["right"] == b2["left"]:
                        neighbors.add(tid2)
                        break
            if (tile_id, tuple(map(tuple, orient))) not in tile_neighbors:
                tile_neighbors[(tile_id, tuple(map(tuple, orient)))] = neighbors

    corners = []
    for tile_id in tiles:
        neighbor_count = len(set(tid for (tid, orient), neighs in tile_neighbors.items() if tid == tile_id for n in [neighs]))
        min_neighbors = min(len(neighs) for (tid, orient), neighs in tile_neighbors.items() if tid == tile_id)
        if min_neighbors == 2:
            corners.append(tile_id)
            break

    for tile_id in tiles:
        found = False
        for orient in all_orientations(tiles[tile_id]):
            neighbors = set()
            b1 = get_borders(orient)
            for tid2, grid2 in tiles.items():
                if tile_id == tid2:
                    continue
                for orient2 in all_orientations(grid2):
                    b2 = get_borders(orient2)
                    if b1["top"] == b2["bottom"] or b1["bottom"] == b2["top"] or \
                       b1["left"] == b2["right"] or b1["right"] == b2["left"]:
                        neighbors.add(tid2)
                        break
            if len(neighbors) == 2 and b1["top"] not in [get_borders(o)["bottom"] for tid, g in tiles.items() if tid != tile_id for o in all_orientations(g)] and \
               b1["left"] not in [get_borders(o)["right"] for tid, g in tiles.items() if tid != tile_id for o in all_orientations(g)]:
                start_tile = tile_id
                start_orient = orient
                found = True
                break
        if found:
            break

    grid_size = int(math.sqrt(len(tiles)))
    placed = {}
    placed[(0, 0)] = (start_tile, start_orient)
    used = {start_tile}

    for row in range(grid_size):
        for col in range(grid_size):
            if (row, col) in placed:
                continue

            if col > 0:
                left_tid, left_grid = placed[(row, col-1)]
                left_border = get_borders(left_grid)["right"]
                for tid in tiles:
                    if tid in used:
                        continue
                    for orient in all_orientations(tiles[tid]):
                        if get_borders(orient)["left"] == left_border:
                            if row > 0:
                                top_tid, top_grid = placed[(row-1, col)]
                                top_border = get_borders(top_grid)["bottom"]
                                if get_borders(orient)["top"] == top_border:
                                    placed[(row, col)] = (tid, orient)
                                    used.add(tid)
                                    break
                            else:
                                placed[(row, col)] = (tid, orient)
                                used.add(tid)
                                break
                    if (row, col) in placed:
                        break
            elif row > 0:
                top_tid, top_grid = placed[(row-1, col)]
                top_border = get_borders(top_grid)["bottom"]
                for tid in tiles:
                    if tid in used:
                        continue
                    for orient in all_orientations(tiles[tid]):
                        if get_borders(orient)["top"] == top_border:
                            placed[(row, col)] = (tid, orient)
                            used.add(tid)
                            break
                    if (row, col) in placed:
                        break

    tile_size = len(tiles[start_tile])
    inner_size = tile_size - 2
    full_size = grid_size * inner_size

    full_image = [['.' for _ in range(full_size)] for _ in range(full_size)]

    for row in range(grid_size):
        for col in range(grid_size):
            tid, grid = placed[(row, col)]
            for i in range(1, tile_size - 1):
                for j in range(1, tile_size - 1):
                    full_image[row * inner_size + i - 1][col * inner_size + j - 1] = grid[i][j]

    monster = [
        "                  # ",
        "#    ##    ##    ###",
        " #  #  #  #  #  #   "
    ]
    monster_coords = []
    for i, line in enumerate(monster):
        for j, char in enumerate(line):
            if char == '#':
                monster_coords.append((i, j))

    def count_monsters(image):
        count = 0
        rows = len(image)
        cols = len(image[0])
        for i in range(rows - 2):
            for j in range(cols - 19):
                if all(image[i + di][j + dj] == '#' for di, dj in monster_coords):
                    count += 1
        return count

    max_monsters = 0
    for orient in all_orientations(full_image):
        monsters = count_monsters(orient)
        if monsters > max_monsters:
            max_monsters = monsters

    total_hash = sum(row.count('#') for row in full_image)
    monster_hash = len(monster_coords)
    answer = total_hash - max_monsters * monster_hash

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
