from aoc.helper import AOC
import heapq
from itertools import count

@AOC.puzzle(2021, 23, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """#############
# #...........#
# ###B#C#B#D###
#   #D#C#B#A#
#   #D#B#A#C#
#   #A#D#C#A#
#   #########""".splitlines()

    energy = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}
    room_col = {'A': 3, 'B': 5, 'C': 7, 'D': 9}
    room_depth = 4

    def parse(lines):
        state = {}
        for row_idx, line in enumerate(lines):
            for col_idx, char in enumerate(line):
                if char in 'ABCD':
                    state[(row_idx, col_idx)] = char
        return state

    def is_done(state):
        expected = {}
        for amphipod, col in room_col.items():
            for row in range(2, 2 + room_depth):
                expected[(row, col)] = amphipod
        return state == expected

    def room_ready(state, amphipod):
        col = room_col[amphipod]
        for r in range(2, 2 + room_depth):
            if (r, col) in state:
                if state[(r, col)] != amphipod:
                    return False
        return True

    def room_has_wrong(state, col):
        for r in range(2, 2 + room_depth):
            if (r, col) in state:
                correct_type = [k for k, v in room_col.items() if v == col][0]
                if state[(r, col)] != correct_type:
                    return True
        return False

    def get_topmost_in_room(state, col):
        for r in range(2, 2 + room_depth):
            if (r, col) in state:
                return r
        return None

    def get_empty_spot_in_room(state, col):
        for r in range(2 + room_depth - 1, 1, -1):
            if (r, col) not in state:
                return r
        return None

    def moves(state):
        result = []

        for pos, amphipod in list(state.items()):
            row, col = pos

            if row == 1:
                target_col = room_col[amphipod]
                if not room_ready(state, amphipod):
                    continue

                path_cols = list(range(min(col, target_col), max(col, target_col) + 1))
                path_cols.remove(col)
                if any((1, c) in state for c in path_cols):
                    continue

                target_row = get_empty_spot_in_room(state, target_col)
                if target_row is None:
                    continue

                steps_down = target_row - 1
                steps = abs(col - target_col) + steps_down
                cost = steps * energy[amphipod]
                new_state = dict(state)
                del new_state[pos]
                new_state[(target_row, target_col)] = amphipod
                result.append((cost, new_state))

            elif row >= 2:
                correct_col = room_col[amphipod]
                if col == correct_col and not room_has_wrong(state, col):
                    continue

                topmost = get_topmost_in_room(state, col)
                if topmost != row:
                    continue

                steps_to_hallway = row - 1

                for target_col in [1, 2, 4, 6, 8, 10, 11]:
                    if col < target_col:
                        path_cols = list(range(col, target_col + 1))
                    else:
                        path_cols = list(range(target_col, col + 1))

                    if any((1, c) in state and c != col for c in path_cols):
                        continue

                    steps = steps_to_hallway + abs(col - target_col)
                    cost = steps * energy[amphipod]
                    new_state = dict(state)
                    del new_state[pos]
                    new_state[(1, target_col)] = amphipod
                    result.append((cost, new_state))

        return result

    lines = list(data)
    if len(lines) == 5:
        extra_lines = [
            "  #D#C#B#A#",
            "  #D#B#A#C#"
        ]
        lines = lines[:3] + extra_lines + lines[3:]

    initial = parse(lines)

    counter = count()
    pq = [(0, next(counter), frozenset(initial.items()))]
    visited = set()

    while pq:
        cost, _, state_frozen = heapq.heappop(pq)

        if state_frozen in visited:
            continue
        visited.add(state_frozen)

        state = dict(state_frozen)

        if is_done(state):
            answer = cost
            print(f"Found answer: {answer}")
            AOC.submit_answer(answer)
            return

        for move_cost, new_state in moves(state):
            total_cost = cost + move_cost
            heapq.heappush(pq, (total_cost, next(counter), frozenset(new_state.items())))

if __name__ == "__main__":
    solve()
