from aoc.helper import AOC
import heapq


def simulate_combat(boss_hp, boss_damage):
    spells = {
        "Magic Missile": (53, lambda s: {**s, "boss_hp": s["boss_hp"] - 4}),
        "Drain": (73, lambda s: {**s, "boss_hp": s["boss_hp"] - 2, "player_hp": s["player_hp"] + 2}),
        "Shield": (113, lambda s: {**s, "shield_timer": 6}),
        "Poison": (173, lambda s: {**s, "poison_timer": 6}),
        "Recharge": (229, lambda s: {**s, "recharge_timer": 5}),
    }

    def apply_effects(state):
        s = state.copy()
        if s["poison_timer"] > 0:
            s["boss_hp"] -= 3
            s["poison_timer"] -= 1
        if s["recharge_timer"] > 0:
            s["player_mana"] += 101
            s["recharge_timer"] -= 1
        if s["shield_timer"] > 0:
            s["shield_timer"] -= 1
        return s

    initial = {
        "player_hp": 50,
        "player_mana": 500,
        "boss_hp": boss_hp,
        "shield_timer": 0,
        "poison_timer": 0,
        "recharge_timer": 0,
        "mana_spent": 0,
        "player_turn": True,
    }

    heap = [(0, 0, initial)]
    visited = set()
    counter = 0

    while heap:
        mana_spent, _, state = heapq.heappop(heap)

        if state["boss_hp"] <= 0:
            return mana_spent

        if state["player_hp"] <= 0:
            continue

        state_key = (
            state["player_hp"],
            state["player_mana"],
            state["boss_hp"],
            state["shield_timer"],
            state["poison_timer"],
            state["recharge_timer"],
            state["player_turn"],
        )

        if state_key in visited:
            continue
        visited.add(state_key)

        state = apply_effects(state)

        if state["boss_hp"] <= 0:
            return mana_spent

        if state["player_turn"]:
            for spell_name, (cost, effect) in spells.items():
                if cost > state["player_mana"]:
                    continue

                if spell_name == "Shield" and state["shield_timer"] > 0:
                    continue
                if spell_name == "Poison" and state["poison_timer"] > 0:
                    continue
                if spell_name == "Recharge" and state["recharge_timer"] > 0:
                    continue

                new_state = effect(state)
                new_state["player_mana"] -= cost
                new_state["mana_spent"] += cost
                new_state["player_turn"] = False

                counter += 1
                heapq.heappush(heap, (new_state["mana_spent"], counter, new_state))
        else:
            armor = 7 if state["shield_timer"] > 0 else 0
            damage = max(1, boss_damage - armor)

            new_state = state.copy()
            new_state["player_hp"] -= damage
            new_state["player_turn"] = True

            counter += 1
            heapq.heappush(heap, (mana_spent, counter, new_state))

    return -1


@AOC.puzzle(2015, 22, 1)
def solve():
    data = AOC.get_data().strip()
    lines = data.split('\n')
    boss_hp = int(lines[0].split(': ')[1])
    boss_damage = int(lines[1].split(': ')[1])

    result = simulate_combat(boss_hp, boss_damage)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
