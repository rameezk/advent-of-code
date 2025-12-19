from aoc.helper import AOC
from itertools import combinations


@AOC.puzzle(2015, 21, 1)
def solve():
    data = AOC.get_data().strip()

    lines = data.split('\n')
    boss_hp = int(lines[0].split(': ')[1])
    boss_damage = int(lines[1].split(': ')[1])
    boss_armor = int(lines[2].split(': ')[1])

    weapons = [
        (8, 4, 0),
        (10, 5, 0),
        (25, 6, 0),
        (40, 7, 0),
        (74, 8, 0),
    ]

    armor = [
        (0, 0, 0),
        (13, 0, 1),
        (31, 0, 2),
        (53, 0, 3),
        (75, 0, 4),
        (102, 0, 5),
    ]

    rings = [
        (0, 0, 0),
        (25, 1, 0),
        (50, 2, 0),
        (100, 3, 0),
        (20, 0, 1),
        (40, 0, 2),
        (80, 0, 3),
    ]

    def simulate_battle(player_hp, player_damage, player_armor, boss_hp, boss_damage, boss_armor):
        player_hp_current = player_hp
        boss_hp_current = boss_hp

        while True:
            damage_to_boss = max(1, player_damage - boss_armor)
            boss_hp_current -= damage_to_boss
            if boss_hp_current <= 0:
                return True

            damage_to_player = max(1, boss_damage - player_armor)
            player_hp_current -= damage_to_player
            if player_hp_current <= 0:
                return False

    min_cost = float('inf')

    for weapon in weapons:
        for armor_piece in armor:
            for num_rings in [0, 1, 2]:
                if num_rings == 0:
                    ring_combos = [[(0, 0, 0)]]
                elif num_rings == 1:
                    ring_combos = [[r] for r in rings]
                else:
                    ring_combos = list(combinations(rings, 2))

                for ring_combo in ring_combos:
                    total_cost = weapon[0] + armor_piece[0]
                    total_damage = weapon[1] + armor_piece[1]
                    total_armor = weapon[2] + armor_piece[2]

                    for ring in ring_combo:
                        total_cost += ring[0]
                        total_damage += ring[1]
                        total_armor += ring[2]

                    if simulate_battle(100, total_damage, total_armor, boss_hp, boss_damage, boss_armor):
                        min_cost = min(min_cost, total_cost)

    AOC.submit_answer(min_cost)


if __name__ == "__main__":
    solve()
