from aoc.helper import AOC


@AOC.puzzle(2018, 13, 2)
def solve():
    data = AOC.get_data()

#     data = r"""/>-<\
# |   |
# | /<+-\
# | | | v
# \>+</ |
#   |   ^
#   \<->/"""

    lines = data.split('\n')

    grid = {}
    carts = []

    for y, line in enumerate(lines):
        for x, char in enumerate(line):
            if char in '^v<>':
                if char == '^':
                    carts.append({'x': x, 'y': y, 'dir': 0, 'turn_count': 0, 'crashed': False})
                    grid[(x, y)] = '|'
                elif char == 'v':
                    carts.append({'x': x, 'y': y, 'dir': 2, 'turn_count': 0, 'crashed': False})
                    grid[(x, y)] = '|'
                elif char == '<':
                    carts.append({'x': x, 'y': y, 'dir': 3, 'turn_count': 0, 'crashed': False})
                    grid[(x, y)] = '-'
                elif char == '>':
                    carts.append({'x': x, 'y': y, 'dir': 1, 'turn_count': 0, 'crashed': False})
                    grid[(x, y)] = '-'
            elif char != ' ':
                grid[(x, y)] = char

    directions = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    while True:
        active_carts = [c for c in carts if not c['crashed']]
        if len(active_carts) == 1:
            result = f"{active_carts[0]['x']},{active_carts[0]['y']}"
            print(result)
            AOC.submit_answer(result)
            return

        carts.sort(key=lambda c: (c['y'], c['x']))

        for cart in carts:
            if cart['crashed']:
                continue

            dx, dy = directions[cart['dir']]
            cart['x'] += dx
            cart['y'] += dy

            for other in carts:
                if other is not cart and not other['crashed'] and other['x'] == cart['x'] and other['y'] == cart['y']:
                    cart['crashed'] = True
                    other['crashed'] = True
                    break

            if cart['crashed']:
                continue

            pos = (cart['x'], cart['y'])
            track = grid[pos]

            if track == '/':
                if cart['dir'] == 0:
                    cart['dir'] = 1
                elif cart['dir'] == 1:
                    cart['dir'] = 0
                elif cart['dir'] == 2:
                    cart['dir'] = 3
                elif cart['dir'] == 3:
                    cart['dir'] = 2
            elif track == '\\':
                if cart['dir'] == 0:
                    cart['dir'] = 3
                elif cart['dir'] == 1:
                    cart['dir'] = 2
                elif cart['dir'] == 2:
                    cart['dir'] = 1
                elif cart['dir'] == 3:
                    cart['dir'] = 0
            elif track == '+':
                if cart['turn_count'] % 3 == 0:
                    cart['dir'] = (cart['dir'] - 1) % 4
                elif cart['turn_count'] % 3 == 2:
                    cart['dir'] = (cart['dir'] + 1) % 4
                cart['turn_count'] += 1


if __name__ == "__main__":
    solve()
