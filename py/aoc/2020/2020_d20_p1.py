from aoc.helper import AOC

@AOC.puzzle(2020, 20, 1)
def solve():
    data = AOC.get_data().strip()

    tiles = {}
    for tile_block in data.split("\n\n"):
        lines = tile_block.strip().split("\n")
        tile_id = int(lines[0].split()[1].rstrip(":"))
        grid = [list(line) for line in lines[1:]]
        tiles[tile_id] = grid

    def get_borders(grid):
        top = "".join(grid[0])
        bottom = "".join(grid[-1])
        left = "".join(row[0] for row in grid)
        right = "".join(row[-1] for row in grid)
        return [top, right, bottom, left]

    def get_all_borders(grid):
        borders = get_borders(grid)
        return borders + [b[::-1] for b in borders]

    border_map = {}
    for tile_id, grid in tiles.items():
        all_borders = get_all_borders(grid)
        for border in all_borders:
            if border not in border_map:
                border_map[border] = []
            border_map[border].append(tile_id)

    tile_neighbors = {}
    for tile_id, grid in tiles.items():
        borders = get_borders(grid)
        neighbors = set()
        for border in borders:
            if border in border_map:
                for neighbor_id in border_map[border]:
                    if neighbor_id != tile_id:
                        neighbors.add(neighbor_id)
            rev_border = border[::-1]
            if rev_border in border_map:
                for neighbor_id in border_map[rev_border]:
                    if neighbor_id != tile_id:
                        neighbors.add(neighbor_id)
        tile_neighbors[tile_id] = neighbors

    corner_tiles = []
    for tile_id, neighbors in tile_neighbors.items():
        if len(neighbors) == 2:
            corner_tiles.append(tile_id)

    answer = 1
    for tile_id in corner_tiles:
        answer *= tile_id

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
