from aoc.helper import AOC


@AOC.puzzle(2018, 5, 2)
def solve():
    data = AOC.get_data().strip()

#     data = """dabAcCaCBAcCcaDA"""

    def react_polymer(polymer):
        stack = []
        for unit in polymer:
            if stack and stack[-1] != unit and stack[-1].lower() == unit.lower():
                stack.pop()
            else:
                stack.append(unit)
        return ''.join(stack)

    unique_units = set(data.lower())

    min_length = float('inf')

    for unit in unique_units:
        filtered = ''.join(c for c in data if c.lower() != unit)
        reacted = react_polymer(filtered)
        min_length = min(min_length, len(reacted))

    answer = min_length

    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
