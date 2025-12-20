from aoc.helper import AOC


@AOC.puzzle(2018, 12, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """initial state: #..#.#..##......###...###
#
# ...## => #
# ..#.. => #
# .#... => #
# .#.#. => #
# .#.## => #
# .##.. => #
# .#### => #
# #.#.# => #
# #.### => #
# ##.#. => #
# ##.## => #
# ###.. => #
# ###.# => #
# ####. => #""".strip().splitlines()

    initial_state = data[0].split(": ")[1]

    rules = {}
    for line in data[2:]:
        pattern, result = line.split(" => ")
        rules[pattern] = result

    state = {}
    for i, c in enumerate(initial_state):
        if c == '#':
            state[i] = True

    target = 50000000000

    prev_sum = 0
    prev_diff = 0
    stable_count = 0

    for generation in range(1, target + 1):
        new_state = {}

        min_pot = min(state.keys())
        max_pot = max(state.keys())

        for pot in range(min_pot - 2, max_pot + 3):
            pattern = ""
            for offset in [-2, -1, 0, 1, 2]:
                pattern += '#' if state.get(pot + offset, False) else '.'

            if rules.get(pattern) == '#':
                new_state[pot] = True

        state = new_state

        current_sum = sum(state.keys())
        diff = current_sum - prev_sum

        if diff == prev_diff:
            stable_count += 1
            if stable_count >= 10:
                remaining = target - generation
                result = current_sum + (diff * remaining)
                print(result)
                AOC.submit_answer(result)
                return
        else:
            stable_count = 0

        prev_sum = current_sum
        prev_diff = diff


if __name__ == "__main__":
    solve()
