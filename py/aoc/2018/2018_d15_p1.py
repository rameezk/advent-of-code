from aoc.helper import AOC
from collections import deque


@AOC.puzzle(2018, 15, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """#######
# #.G...#
# #...EG#
# #.#.#G#
# #..G#E#
# #.....#
# #######"""

#     data = """#######
# #G..#E#
# #E#E.E#
# #G.##.#
# #...#E#
# #...E.#
# #######"""

#     data = """#######
# #E..EG#
# #.#G.E#
# #E.##E#
# #G..#.#
# #..E#.#
# #######"""

#     data = """#######
# #E.G#.#
# #.#G..#
# #G.#.G#
# #G..#.#
# #...E.#
# #######"""

#     data = """#######
# #.E...#
# #.#..G#
# #.###.#
# #E#G#G#
# #...#G#
# #######"""

#     data = """#########
# #G......#
# #.E.#...#
# #..##..G#
# #...##..#
# #...#...#
# #.G...G.#
# #.....G.#
# #########"""

    class Unit:
        def __init__(self, x, y, type, attack_power=3):
            self.x = x
            self.y = y
            self.type = type
            self.hp = 200
            self.attack_power = attack_power

        def is_alive(self):
            return self.hp > 0

        def __repr__(self):
            return f"{self.type}({self.hp})"

    def parse_map(data):
        lines = data.strip().split('\n')
        grid = []
        units = []

        for y, line in enumerate(lines):
            row = []
            for x, char in enumerate(line):
                if char in ['E', 'G']:
                    units.append(Unit(x, y, char))
                    row.append('.')
                else:
                    row.append(char)
            grid.append(row)

        return grid, units

    def get_targets(unit, units):
        enemy_type = 'G' if unit.type == 'E' else 'E'
        return [u for u in units if u.type == enemy_type and u.is_alive()]

    def get_in_range(targets, grid, units):
        in_range = set()
        occupied = {(u.x, u.y) for u in units if u.is_alive()}

        for target in targets:
            for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                nx, ny = target.x + dx, target.y + dy
                if grid[ny][nx] == '.' and (nx, ny) not in occupied:
                    in_range.add((nx, ny))

        return in_range

    def bfs_distance(start, end, grid, units):
        occupied = {(u.x, u.y) for u in units if u.is_alive()}
        if start in occupied:
            occupied.remove(start)

        queue = deque([(start, 0)])
        visited = {start}

        while queue:
            pos, dist = queue.popleft()

            if pos == end:
                return dist

            for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
                nx, ny = pos[0] + dx, pos[1] + dy
                next_pos = (nx, ny)

                if (next_pos not in visited and
                    grid[ny][nx] == '.' and
                    next_pos not in occupied):
                    visited.add(next_pos)
                    queue.append((next_pos, dist + 1))

        return float('inf')

    def find_next_step(start, goal, grid, units):
        occupied = {(u.x, u.y) for u in units if u.is_alive()}
        if start in occupied:
            occupied.remove(start)

        best_steps = []

        for dx, dy in [(0, -1), (-1, 0), (1, 0), (0, 1)]:
            nx, ny = start[0] + dx, start[1] + dy
            next_pos = (nx, ny)

            if grid[ny][nx] == '.' and next_pos not in occupied:
                dist = bfs_distance(next_pos, goal, grid, units)
                if dist < float('inf'):
                    best_steps.append((dist, ny, nx, next_pos))

        if not best_steps:
            return None

        best_steps.sort()
        return best_steps[0][3]

    def move_unit(unit, targets, grid, units):
        if get_attack_target(unit, units):
            return

        in_range = get_in_range(targets, grid, units)

        if not in_range:
            return

        current_pos = (unit.x, unit.y)

        reachable = []
        for pos in in_range:
            dist = bfs_distance(current_pos, pos, grid, units)
            if dist < float('inf'):
                reachable.append((dist, pos[1], pos[0], pos))

        if not reachable:
            return

        reachable.sort()
        chosen = reachable[0][3]

        next_step = find_next_step(current_pos, chosen, grid, units)

        if next_step:
            unit.x, unit.y = next_step

    def get_attack_target(unit, units):
        adjacent = []
        enemy_type = 'G' if unit.type == 'E' else 'E'

        for target in units:
            if not target.is_alive() or target.type != enemy_type:
                continue

            if abs(target.x - unit.x) + abs(target.y - unit.y) == 1:
                adjacent.append(target)

        if not adjacent:
            return None

        adjacent.sort(key=lambda u: (u.hp, u.y, u.x))
        return adjacent[0]

    def attack(unit, target):
        target.hp -= unit.attack_power

    def simulate_combat(grid, units):
        rounds = 0

        while True:
            units.sort(key=lambda u: (u.y, u.x))
            completed_round = True

            for i, unit in enumerate(units):
                if not unit.is_alive():
                    continue

                targets = get_targets(unit, units)

                if not targets:
                    units[:] = [u for u in units if u.is_alive()]
                    return rounds, sum(u.hp for u in units)

                move_unit(unit, targets, grid, units)

                target = get_attack_target(unit, units)
                if target:
                    attack(unit, target)

            units[:] = [u for u in units if u.is_alive()]
            rounds += 1

    grid, units = parse_map(data)
    rounds, total_hp = simulate_combat(grid, units)
    outcome = rounds * total_hp

    print(f"Rounds: {rounds}, Total HP: {total_hp}, Outcome: {outcome}")
    AOC.submit_answer(outcome)


if __name__ == "__main__":
    solve()
