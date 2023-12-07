from aoc.helper import download_input, submit_answer

from enum import IntEnum

from collections import Counter, defaultdict


class HandType(IntEnum):
    HighCard = 1
    OnePair = 2
    TwoPair = 3
    ThreeOfAKind = 4
    FullHouse = 5
    FourOfAKind = 6
    FiveOfAKind = 7


def get_hand_type(hand: str) -> HandType:
    c = Counter(hand).values()
    cc = Counter(c)

    if cc[1] == 5:
        return HandType.HighCard

    if cc[1] == 3 and cc[2] == 1:
        return HandType.OnePair

    if cc[1] == 1 and cc[2] == 2:
        return HandType.TwoPair

    if cc[1] == 2 and cc[3] == 1:
        return HandType.ThreeOfAKind

    if cc[2] == 1 and cc[3] == 1:
        return HandType.FullHouse

    if cc[4] == 1 and cc[1] == 1:
        return HandType.FourOfAKind

    if cc[5] == 1:
        return HandType.FiveOfAKind

    raise Exception("Unknown hand type")


def sort_by_hand_strength(hands: list) -> list:
    s = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
    return sorted(hands, key=lambda h: [s.index(c) for c in h], reverse=True)


if __name__ == "__main__":
    download_input(2023, 7)

    with open("./2023_d07.txt") as f:
        cards = f.read().strip().splitlines()

    #         cards = """
    # 32T3K 765
    # T55J5 684
    # KK677 28
    # KTJJT 220
    # QQQJA 483
    #         """.strip().splitlines()

    H = {}
    for card in cards:
        hand, bid = card.split()
        bid = int(bid)
        H[hand] = bid

    L = defaultdict(lambda: [])
    for hand, bid in H.items():
        t = get_hand_type(hand)
        L[t].append(hand)

    L = dict(sorted(L.items()))

    R = {}
    C = 0
    for t, hands in L.items():
        sh = sort_by_hand_strength(hands)

        for hand in sh:
            C += 1
            if hand in R:
                raise Exception(f"{hand} already there")
            R[hand] = C

    W = 0
    for hand, rank in R.items():
        W += H[hand] * rank

    print(W)
    # submit_answer(2023, 7, 1, W)
