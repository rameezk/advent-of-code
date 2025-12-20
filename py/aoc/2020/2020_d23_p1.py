from aoc.helper import AOC

@AOC.puzzle(2020, 23, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """389125467"""

    cups = [int(x) for x in data]
    n = len(cups)

    current_idx = 0

    for move in range(100):
        current_cup = cups[current_idx]

        pick_up = []
        for i in range(3):
            pick_idx = (current_idx + 1) % len(cups)
            pick_up.append(cups.pop(pick_idx))
            if pick_idx <= current_idx:
                current_idx -= 1

        destination = current_cup - 1
        if destination < 1:
            destination = n
        while destination in pick_up:
            destination -= 1
            if destination < 1:
                destination = n

        dest_idx = cups.index(destination)

        for i, cup in enumerate(pick_up):
            cups.insert(dest_idx + 1 + i, cup)
            if dest_idx + 1 + i <= current_idx:
                current_idx += 1

        current_idx = (current_idx + 1) % len(cups)

    one_idx = cups.index(1)
    result = []
    for i in range(1, len(cups)):
        result.append(str(cups[(one_idx + i) % len(cups)]))

    answer = ''.join(result)
    print(f"Answer: {answer}")

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
