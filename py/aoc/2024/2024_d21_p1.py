from aoc.helper import AOC
from functools import cache
from collections import deque


@AOC.puzzle(2024, 21, 1)
def solve():
#     data = """029A
# 980A
# 179A
# 456A
# 379A"""

    data = AOC.get_data().strip()

    numeric_keypad = {
        '7': (0, 0), '8': (0, 1), '9': (0, 2),
        '4': (1, 0), '5': (1, 1), '6': (1, 2),
        '1': (2, 0), '2': (2, 1), '3': (2, 2),
        '0': (3, 1), 'A': (3, 2)
    }

    directional_keypad = {
        '^': (0, 1), 'A': (0, 2),
        '<': (1, 0), 'v': (1, 1), '>': (1, 2)
    }

    def get_all_paths(keypad, start, end):
        if start == end:
            return ['A']

        start_pos = keypad[start]
        end_pos = keypad[end]

        dr = end_pos[0] - start_pos[0]
        dc = end_pos[1] - start_pos[1]

        moves = []
        if dr > 0:
            moves.extend(['v'] * dr)
        elif dr < 0:
            moves.extend(['^'] * abs(dr))

        if dc > 0:
            moves.extend(['>'] * dc)
        elif dc < 0:
            moves.extend(['<'] * abs(dc))

        gap_positions = set()
        for key, pos in keypad.items():
            gap_positions.add(pos)

        all_positions = {(0, 0), (0, 1), (0, 2), (1, 0), (1, 1), (1, 2), (2, 0), (2, 1), (2, 2), (3, 0), (3, 1), (3, 2)}
        if keypad == numeric_keypad:
            gap_pos = (3, 0)
        else:
            gap_pos = (0, 0)

        from itertools import permutations
        paths = []
        for perm in set(permutations(moves)):
            pos = start_pos
            valid = True
            for move in perm:
                if move == '^':
                    pos = (pos[0] - 1, pos[1])
                elif move == 'v':
                    pos = (pos[0] + 1, pos[1])
                elif move == '<':
                    pos = (pos[0], pos[1] - 1)
                elif move == '>':
                    pos = (pos[0], pos[1] + 1)

                if pos == gap_pos:
                    valid = False
                    break

            if valid:
                paths.append(''.join(perm) + 'A')

        return paths if paths else ['A']

    @cache
    def min_length_at_level(sequence, level):
        if level == 0:
            return len(sequence)

        keypad = directional_keypad
        total = 0
        current = 'A'

        for char in sequence:
            paths = get_all_paths(keypad, current, char)
            min_len = float('inf')
            for path in paths:
                length = min_length_at_level(path, level - 1)
                min_len = min(min_len, length)
            total += min_len
            current = char

        return total

    def solve_code(code, levels):
        current = 'A'
        total = 0

        for char in code:
            paths = get_all_paths(numeric_keypad, current, char)
            min_len = float('inf')
            for path in paths:
                length = min_length_at_level(path, levels)
                min_len = min(min_len, length)
            total += min_len
            current = char

        return total

    codes = data.strip().split('\n')
    total_complexity = 0

    for code in codes:
        min_length = solve_code(code, 2)
        numeric_part = int(code[:-1])
        complexity = min_length * numeric_part
        print(f"{code}: {min_length} * {numeric_part} = {complexity}")
        total_complexity += complexity

    print(total_complexity)
    AOC.submit_answer(total_complexity)


if __name__ == "__main__":
    solve()
