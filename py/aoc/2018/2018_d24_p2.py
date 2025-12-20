from aoc.helper import AOC
import re
import copy


@AOC.puzzle(2018, 24, 2)
def solve():
    data = AOC.get_data().strip()

#     data = """Immune System:
# 17 units each with 5390 hit points (weak to radiation, bludgeoning) with an attack that does 4507 fire damage at initiative 2
# 989 units each with 1274 hit points (immune to fire; weak to bludgeoning, slashing) with an attack that does 25 slashing damage at initiative 3
#
# Infection:
# 801 units each with 4706 hit points (weak to radiation) with an attack that does 116 bludgeoning damage at initiative 1
# 4485 units each with 2961 hit points (immune to radiation; weak to fire, cold) with an attack that does 12 slashing damage at initiative 4"""

    def parse_input(data):
        lines = data.strip().split('\n')
        immune_system = []
        infection = []

        current_army = None
        for line in lines:
            if line.startswith('Immune System:'):
                current_army = immune_system
            elif line.startswith('Infection:'):
                current_army = infection
            elif line.strip() == '':
                continue
            else:
                match = re.match(
                    r'(\d+) units each with (\d+) hit points (\([^)]+\) )?with an attack that does (\d+) (\w+) damage at initiative (\d+)',
                    line
                )
                if match:
                    units = int(match.group(1))
                    hp = int(match.group(2))
                    modifiers = match.group(3)
                    damage = int(match.group(4))
                    attack_type = match.group(5)
                    initiative = int(match.group(6))

                    weaknesses = []
                    immunities = []

                    if modifiers:
                        modifiers = modifiers.strip('() ')
                        parts = modifiers.split('; ')
                        for part in parts:
                            if part.startswith('weak to '):
                                weaknesses = [x.strip() for x in part[8:].split(', ')]
                            elif part.startswith('immune to '):
                                immunities = [x.strip() for x in part[10:].split(', ')]

                    group = {
                        'units': units,
                        'hp': hp,
                        'damage': damage,
                        'attack_type': attack_type,
                        'initiative': initiative,
                        'weaknesses': weaknesses,
                        'immunities': immunities
                    }
                    current_army.append(group)

        return immune_system, infection

    def effective_power(group):
        return group['units'] * group['damage']

    def calculate_damage(attacker, defender):
        damage = effective_power(attacker)
        if attacker['attack_type'] in defender['immunities']:
            return 0
        if attacker['attack_type'] in defender['weaknesses']:
            return damage * 2
        return damage

    def fight(immune_system, infection):
        while immune_system and infection:
            all_groups = []
            for i, g in enumerate(immune_system):
                all_groups.append((i, 'immune', g))
            for i, g in enumerate(infection):
                all_groups.append((i, 'infection', g))

            all_groups.sort(key=lambda x: (effective_power(x[2]), x[2]['initiative']), reverse=True)

            targets = []
            targeted = set()

            for idx, army_type, group in all_groups:
                if army_type == 'immune':
                    enemies = infection
                    enemy_type = 'infection'
                else:
                    enemies = immune_system
                    enemy_type = 'immune'

                best_target = None
                best_damage = 0

                for i, enemy in enumerate(enemies):
                    if (i, enemy_type) in targeted:
                        continue

                    damage = calculate_damage(group, enemy)
                    if damage == 0:
                        continue

                    if damage > best_damage or (
                        damage == best_damage and best_target is not None and
                        (effective_power(enemy) > effective_power(enemies[best_target]) or
                         (effective_power(enemy) == effective_power(enemies[best_target]) and
                          enemy['initiative'] > enemies[best_target]['initiative']))
                    ):
                        best_target = i
                        best_damage = damage

                if best_target is not None:
                    targets.append((idx, army_type, best_target, enemy_type, group))
                    targeted.add((best_target, enemy_type))

            targets.sort(key=lambda x: x[4]['initiative'], reverse=True)

            units_killed = 0
            for attacker_idx, attacker_army, target_idx, target_army, attacker in targets:
                if attacker_army == 'immune':
                    if attacker_idx >= len(immune_system) or immune_system[attacker_idx]['units'] <= 0:
                        continue
                    attacker = immune_system[attacker_idx]
                    defender = infection[target_idx]
                else:
                    if attacker_idx >= len(infection) or infection[attacker_idx]['units'] <= 0:
                        continue
                    attacker = infection[attacker_idx]
                    defender = immune_system[target_idx]

                damage = calculate_damage(attacker, defender)
                kills = min(damage // defender['hp'], defender['units'])
                defender['units'] -= kills
                units_killed += kills

            if units_killed == 0:
                return None, None

            immune_system = [g for g in immune_system if g['units'] > 0]
            infection = [g for g in infection if g['units'] > 0]

        return immune_system, infection

    def simulate_with_boost(immune_system_template, infection_template, boost):
        immune_system = copy.deepcopy(immune_system_template)
        infection = copy.deepcopy(infection_template)

        for group in immune_system:
            group['damage'] += boost

        immune_system, infection = fight(immune_system, infection)

        if immune_system is None:
            return None

        if immune_system and not infection:
            return sum(g['units'] for g in immune_system)
        else:
            return None

    immune_system_template, infection_template = parse_input(data)

    boost = 0
    while True:
        result = simulate_with_boost(immune_system_template, infection_template, boost)
        if result is not None:
            print(result)
            AOC.submit_answer(result)
            break
        boost += 1


if __name__ == "__main__":
    solve()
