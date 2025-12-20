from aoc.helper import AOC

@AOC.puzzle(2020, 24, 1)
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

    answer = len(black_tiles)

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
