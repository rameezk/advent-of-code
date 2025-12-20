from aoc.helper import AOC

@AOC.puzzle(2020, 23, 2)
def solve():
    data = AOC.get_data().strip()

#     data = """389125467"""

    initial_cups = [int(x) for x in data]

    total_cups = 1_000_000
    moves = 10_000_000

    next_cup = {}

    for i in range(len(initial_cups) - 1):
        next_cup[initial_cups[i]] = initial_cups[i + 1]

    if total_cups > len(initial_cups):
        next_cup[initial_cups[-1]] = len(initial_cups) + 1
        for i in range(len(initial_cups) + 1, total_cups):
            next_cup[i] = i + 1
        next_cup[total_cups] = initial_cups[0]
    else:
        next_cup[initial_cups[-1]] = initial_cups[0]

    current = initial_cups[0]

    for move in range(moves):
        pick1 = next_cup[current]
        pick2 = next_cup[pick1]
        pick3 = next_cup[pick2]

        next_cup[current] = next_cup[pick3]

        destination = current - 1
        if destination < 1:
            destination = total_cups
        while destination in (pick1, pick2, pick3):
            destination -= 1
            if destination < 1:
                destination = total_cups

        next_cup[pick3] = next_cup[destination]
        next_cup[destination] = pick1

        current = next_cup[current]

    cup1 = next_cup[1]
    cup2 = next_cup[cup1]

    answer = cup1 * cup2
    print(f"Answer: {answer}")
    print(f"Cup 1: {cup1}, Cup 2: {cup2}")

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
