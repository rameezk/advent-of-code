from aoc.helper import AOC
from collections import deque
import re


@AOC.puzzle(2016, 11, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """The first floor contains a hydrogen-compatible microchip and a lithium-compatible microchip.
# The second floor contains a hydrogen generator.
# The third floor contains a lithium generator.
# The fourth floor contains nothing relevant.""".splitlines()

    floors = [set(), set(), set(), set()]
    elements = {}
    elem_id = 0

    for floor_num, line in enumerate(data):
        if "nothing relevant" in line:
            continue

        generators = re.findall(r'(\w+) generator', line)
        for gen in generators:
            if gen not in elements:
                elements[gen] = elem_id
                elem_id += 1
            floors[floor_num].add((elements[gen], 'G'))

        microchips = re.findall(r'(\w+)-compatible microchip', line)
        for chip in microchips:
            if chip not in elements:
                elements[chip] = elem_id
                elem_id += 1
            floors[floor_num].add((elements[chip], 'M'))

    elements['elerium'] = elem_id
    floors[0].add((elem_id, 'G'))
    floors[0].add((elem_id, 'M'))
    elem_id += 1

    elements['dilithium'] = elem_id
    floors[0].add((elem_id, 'G'))
    floors[0].add((elem_id, 'M'))

    initial_state = (0, tuple(frozenset(f) for f in floors))

    def is_valid(state):
        elevator, floors = state
        for floor in floors:
            generators = {item[0] for item in floor if item[1] == 'G'}
            microchips = {item[0] for item in floor if item[1] == 'M'}

            if generators:
                for chip in microchips:
                    if chip not in generators:
                        return False
        return True

    def normalize(state):
        elevator, floors = state

        pairs = {}
        for floor_idx, floor in enumerate(floors):
            for item in floor:
                elem_id, item_type = item
                if elem_id not in pairs:
                    pairs[elem_id] = [None, None]
                if item_type == 'G':
                    pairs[elem_id][0] = floor_idx
                else:
                    pairs[elem_id][1] = floor_idx

        pair_positions = tuple(sorted(tuple(p) for p in pairs.values()))
        return (elevator, pair_positions)

    def get_moves(state):
        elevator, floors = state
        current_floor = list(floors[elevator])
        moves = []

        for direction in [-1, 1]:
            next_floor = elevator + direction
            if next_floor < 0 or next_floor >= 4:
                continue

            for i in range(len(current_floor)):
                new_floors = [set(f) for f in floors]
                new_floors[elevator].remove(current_floor[i])
                new_floors[next_floor].add(current_floor[i])
                new_state = (next_floor, tuple(frozenset(f) for f in new_floors))
                if is_valid(new_state):
                    moves.append(new_state)

            for i in range(len(current_floor)):
                for j in range(i + 1, len(current_floor)):
                    new_floors = [set(f) for f in floors]
                    new_floors[elevator].remove(current_floor[i])
                    new_floors[elevator].remove(current_floor[j])
                    new_floors[next_floor].add(current_floor[i])
                    new_floors[next_floor].add(current_floor[j])
                    new_state = (next_floor, tuple(frozenset(f) for f in new_floors))
                    if is_valid(new_state):
                        moves.append(new_state)

        return moves

    def bfs():
        queue = deque([(initial_state, 0)])
        visited = {normalize(initial_state)}

        goal_floor = frozenset()
        for floor in floors:
            goal_floor |= floor

        while queue:
            state, steps = queue.popleft()

            elevator, floors_state = state
            if elevator == 3 and len(floors_state[3]) == len(goal_floor):
                return steps

            for next_state in get_moves(state):
                norm = normalize(next_state)
                if norm not in visited:
                    visited.add(norm)
                    queue.append((next_state, steps + 1))

        return -1

    result = bfs()
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
