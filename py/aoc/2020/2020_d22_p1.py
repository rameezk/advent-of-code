from aoc.helper import AOC

@AOC.puzzle(2020, 22, 1)
def solve():
    data = AOC.get_data().strip()

    pass

    blocks = data.split("\n\n")

    player1_lines = blocks[0].strip().split("\n")[1:]
    player2_lines = blocks[1].strip().split("\n")[1:]

    deck1 = [int(x) for x in player1_lines]
    deck2 = [int(x) for x in player2_lines]

    while deck1 and deck2:
        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        if card1 > card2:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)

    winning_deck = deck1 if deck1 else deck2

    score = 0
    for i, card in enumerate(reversed(winning_deck)):
        score += card * (i + 1)

    answer = score
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
