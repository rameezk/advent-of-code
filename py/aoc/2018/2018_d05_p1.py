from aoc.helper import AOC


@AOC.puzzle(2018, 5, 1)
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

    result = react_polymer(data)
    answer = len(result)

    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
