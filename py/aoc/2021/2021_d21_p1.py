from aoc.helper import AOC

@AOC.puzzle(2021, 21, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """Player 1 starting position: 4
# Player 2 starting position: 8""".splitlines()

    p1_pos = int(data[0].split(": ")[1])
    p2_pos = int(data[1].split(": ")[1])

    p1_score = 0
    p2_score = 0

    die = 1
    rolls = 0

    player = 1

    while p1_score < 1000 and p2_score < 1000:
        total = 0
        for _ in range(3):
            total += die
            die += 1
            if die > 100:
                die = 1
            rolls += 1

        if player == 1:
            p1_pos = (p1_pos + total - 1) % 10 + 1
            p1_score += p1_pos
            player = 2
        else:
            p2_pos = (p2_pos + total - 1) % 10 + 1
            p2_score += p2_pos
            player = 1

    losing_score = min(p1_score, p2_score)
    answer = losing_score * rolls

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
