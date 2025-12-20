from aoc.helper import AOC

@AOC.puzzle(2020, 24, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """sesenwnenenewseeswwswswwnenewsewsw
# neeenesenwnwwswnenewnwwsewnenwseswesw
# seswneswswsenwwnwse
# nwnwneseeswswnenewneswwnewseswneseene
# swweswneswnenwsewnwneneseenw
# eesenwseswswnenwswnwnwsewwnwsene
# sewnenenenesenwsewnenwwwse
# wenwwweseeeweswwwnwwe
# wsweesenenewnwwnwsenewsenwwsesesenwne
# neeswseenwwswnwswswnw
# nenwswwsewswnenenewsenwsenwnesesenew
# enewnwewneswsewnwswenweswnenwsenwsw
# sweneswneswneneenwnewenewwneswswnese
# swwesenesewenwneswnwwneseswwne
# enesenwswwswneneswsenwnewswseenwsese
# wnwnesenesenenwwnenwsewesewsesesew
# nenewswnwewswnenesenwnesewesw
# eneswnwswnwsenenwnwnwwseeswneewsenese
# neswnwewnwnwseenwseesewsenwsweewe
# wseweeenwnesenwwwswnew""".splitlines()

    def parse_directions(line):
        directions = []
        i = 0
        while i < len(line):
            if line[i] in ['e', 'w']:
                directions.append(line[i])
                i += 1
            else:
                directions.append(line[i:i+2])
                i += 2
        return directions

    def get_tile_position(directions):
        q, r = 0, 0
        for d in directions:
            if d == 'e':
                q += 1
            elif d == 'w':
                q -= 1
            elif d == 'se':
                r += 1
            elif d == 'sw':
                q -= 1
                r += 1
            elif d == 'ne':
                q += 1
                r -= 1
            elif d == 'nw':
                r -= 1
        return (q, r)

    black_tiles = set()

    for line in data:
        directions = parse_directions(line)
        pos = get_tile_position(directions)
        if pos in black_tiles:
            black_tiles.remove(pos)
        else:
            black_tiles.add(pos)

    def get_neighbors(q, r):
        return [
            (q + 1, r),
            (q - 1, r),
            (q, r + 1),
            (q - 1, r + 1),
            (q + 1, r - 1),
            (q, r - 1)
        ]

    def count_black_neighbors(pos, black_tiles):
        count = 0
        for neighbor in get_neighbors(*pos):
            if neighbor in black_tiles:
                count += 1
        return count

    def simulate_day(black_tiles):
        new_black_tiles = set()

        tiles_to_check = set()
        for tile in black_tiles:
            tiles_to_check.add(tile)
            for neighbor in get_neighbors(*tile):
                tiles_to_check.add(neighbor)

        for tile in tiles_to_check:
            black_neighbors = count_black_neighbors(tile, black_tiles)
            is_black = tile in black_tiles

            if is_black and (black_neighbors == 1 or black_neighbors == 2):
                new_black_tiles.add(tile)
            elif not is_black and black_neighbors == 2:
                new_black_tiles.add(tile)

        return new_black_tiles

    for day in range(100):
        black_tiles = simulate_day(black_tiles)

    answer = len(black_tiles)

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
