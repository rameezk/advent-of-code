from aoc.helper import AOC
from functools import lru_cache

@AOC.puzzle(2021, 21, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """Player 1 starting position: 4
# Player 2 starting position: 8""".splitlines()

    p1_start = int(data[0].split(": ")[1])
    p2_start = int(data[1].split(": ")[1])

    @lru_cache(maxsize=None)
    def play(p1_pos, p2_pos, p1_score, p2_score):
        if p1_score >= 21:
            return (1, 0)
        if p2_score >= 21:
            return (0, 1)

        p1_wins = 0
        p2_wins = 0

        for d1 in [1, 2, 3]:
            for d2 in [1, 2, 3]:
                for d3 in [1, 2, 3]:
                    total = d1 + d2 + d3
                    new_pos = (p1_pos + total - 1) % 10 + 1
                    new_score = p1_score + new_pos

                    w2, w1 = play(p2_pos, new_pos, p2_score, new_score)
                    p1_wins += w1
                    p2_wins += w2

        return (p1_wins, p2_wins)

    p1_wins, p2_wins = play(p1_start, p2_start, 0, 0)
    answer = max(p1_wins, p2_wins)

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
