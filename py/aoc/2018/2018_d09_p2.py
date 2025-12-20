from aoc.helper import AOC
from collections import deque


@AOC.puzzle(2018, 9, 2)
def solve():
    data = AOC.get_data().strip()

#     data = """10 players; last marble is worth 1618 points"""

    parts = data.split()
    num_players = int(parts[0])
    last_marble = int(parts[6]) * 100

    circle = deque([0])
    scores = [0] * num_players
    current_player = 0

    for marble in range(1, last_marble + 1):
        if marble % 23 == 0:
            scores[current_player] += marble
            circle.rotate(7)
            scores[current_player] += circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(marble)

        current_player = (current_player + 1) % num_players

    result = max(scores)
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
