from aoc.helper import AOC

@AOC.puzzle(2017, 17, 1)
def solve():
    data = AOC.get_data().strip()
    # data = """3"""

    steps = int(data)

    buffer = [0]
    pos = 0

    for i in range(1, 2018):
        pos = (pos + steps) % len(buffer) + 1
        buffer.insert(pos, i)

    idx_2017 = buffer.index(2017)
    answer = buffer[(idx_2017 + 1) % len(buffer)]

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
