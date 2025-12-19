from aoc.helper import AOC

@AOC.puzzle(2017, 24, 1)
def solve():
    data = AOC.get_data().strip()
    # data = """0/2
# 2/2
# 2/3
# 3/4
# 3/5
# 0/1
# 10/1
# 9/10"""

    components = []
    for line in data.split('\n'):
        a, b = map(int, line.split('/'))
        components.append((a, b))

    def build_bridges(current_port, used, strength):
        max_strength = strength

        for i, (a, b) in enumerate(components):
            if i in used:
                continue

            if a == current_port:
                next_port = b
            elif b == current_port:
                next_port = a
            else:
                continue

            new_used = used | {i}
            new_strength = strength + a + b
            max_strength = max(max_strength, build_bridges(next_port, new_used, new_strength))

        return max_strength

    answer = build_bridges(0, set(), 0)
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
