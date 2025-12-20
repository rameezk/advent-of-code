from aoc.helper import AOC

def play_recursive_combat(deck1, deck2):
    seen_states = set()

    while deck1 and deck2:
        state = (tuple(deck1), tuple(deck2))
        if state in seen_states:
            return 1, deck1
        seen_states.add(state)

        card1 = deck1.pop(0)
        card2 = deck2.pop(0)

        if len(deck1) >= card1 and len(deck2) >= card2:
            new_deck1 = deck1[:card1]
            new_deck2 = deck2[:card2]
            winner, _ = play_recursive_combat(new_deck1, new_deck2)
        else:
            winner = 1 if card1 > card2 else 2

        if winner == 1:
            deck1.append(card1)
            deck1.append(card2)
        else:
            deck2.append(card2)
            deck2.append(card1)

    if deck1:
        return 1, deck1
    else:
        return 2, deck2

@AOC.puzzle(2020, 22, 2)
def solve():
    data = AOC.get_data().strip()

    pass

    blocks = data.split("\n\n")

    player1_lines = blocks[0].strip().split("\n")[1:]
    player2_lines = blocks[1].strip().split("\n")[1:]

    deck1 = [int(x) for x in player1_lines]
    deck2 = [int(x) for x in player2_lines]

    winner, winning_deck = play_recursive_combat(deck1, deck2)

    score = 0
    for i, card in enumerate(reversed(winning_deck)):
        score += card * (i + 1)

    answer = score
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
