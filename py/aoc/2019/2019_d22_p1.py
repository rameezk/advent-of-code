from aoc.helper import AOC


@AOC.puzzle(2019, 22, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

    deck_size = 10007
    position = 2019

    for instruction in data:
        if instruction == "deal into new stack":
            position = deck_size - 1 - position
        elif instruction.startswith("cut "):
            n = int(instruction.split()[1])
            position = (position - n) % deck_size
        elif instruction.startswith("deal with increment "):
            n = int(instruction.split()[-1])
            position = (position * n) % deck_size

    answer = position
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
