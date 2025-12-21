from aoc.helper import AOC
from functools import cache
import re


@AOC.puzzle(2022, 16, 1)
def solve():
    # data = """Valve AA has flow rate=0; tunnels lead to valves DD, II, BB
# Valve BB has flow rate=13; tunnels lead to valves CC, AA
# Valve CC has flow rate=2; tunnels lead to valves DD, BB
# Valve DD has flow rate=20; tunnels lead to valves CC, AA, EE
# Valve EE has flow rate=3; tunnels lead to valves FF, DD
# Valve FF has flow rate=0; tunnels lead to valves EE, GG
# Valve GG has flow rate=0; tunnels lead to valves FF, HH
# Valve HH has flow rate=22; tunnel leads to valve GG
# Valve II has flow rate=0; tunnels lead to valves AA, JJ
# Valve JJ has flow rate=21; tunnel leads to valve II"""

    data = AOC.get_data()

    valves = {}
    flow_rates = {}

    for line in data.strip().splitlines():
        match = re.match(r'Valve (\w+) has flow rate=(\d+); tunnels? leads? to valves? (.+)', line)
        valve = match.group(1)
        flow_rate = int(match.group(2))
        tunnels = match.group(3).split(', ')

        valves[valve] = tunnels
        flow_rates[valve] = flow_rate

    important_valves = {v for v, f in flow_rates.items() if f > 0}
    all_valves = list(valves.keys())
    valve_to_idx = {v: i for i, v in enumerate(all_valves)}

    dist = [[float('inf')] * len(all_valves) for _ in range(len(all_valves))]
    for i in range(len(all_valves)):
        dist[i][i] = 0

    for valve, neighbors in valves.items():
        i = valve_to_idx[valve]
        for neighbor in neighbors:
            j = valve_to_idx[neighbor]
            dist[i][j] = 1

    for k in range(len(all_valves)):
        for i in range(len(all_valves)):
            for j in range(len(all_valves)):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    important_valve_list = sorted(list(important_valves))
    valve_to_bit = {v: i for i, v in enumerate(important_valve_list)}

    @cache
    def dp(current_valve, time_left, opened_mask):
        if time_left <= 0:
            return 0

        max_pressure = 0

        for valve in important_valves:
            bit_pos = valve_to_bit[valve]
            if opened_mask & (1 << bit_pos):
                continue

            travel_time = dist[valve_to_idx[current_valve]][valve_to_idx[valve]]
            time_after_travel = time_left - travel_time - 1

            if time_after_travel <= 0:
                continue

            new_mask = opened_mask | (1 << bit_pos)
            pressure = flow_rates[valve] * time_after_travel
            future_pressure = dp(valve, time_after_travel, new_mask)

            max_pressure = max(max_pressure, pressure + future_pressure)

        return max_pressure

    result = dp('AA', 30, 0)
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
