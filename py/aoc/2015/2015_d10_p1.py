from aoc.helper import AOC


@AOC.puzzle(2015, 10, 1)
def solve():
    data = AOC.get_data().strip()

    # data = """1"""

    def look_and_say(s):
        result = []
        i = 0
        while i < len(s):
            digit = s[i]
            count = 1
            while i + count < len(s) and s[i + count] == digit:
                count += 1
            result.append(str(count) + digit)
            i += count
        return ''.join(result)

    current = data
    for _ in range(40):
        current = look_and_say(current)

    result = len(current)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
