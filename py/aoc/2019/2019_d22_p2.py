from aoc.helper import AOC


def modinv(a, m):
    return pow(a, -1, m)


@AOC.puzzle(2019, 22, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

    deck_size = 119315717514047
    shuffles = 101741582076661
    target_position = 2020

    a, b = 1, 0

    for instruction in data:
        if instruction == "deal into new stack":
            a = -a % deck_size
            b = (deck_size - 1 - b) % deck_size
        elif instruction.startswith("cut "):
            n = int(instruction.split()[1])
            b = (b - n) % deck_size
        elif instruction.startswith("deal with increment "):
            n = int(instruction.split()[-1])
            a = (a * n) % deck_size
            b = (b * n) % deck_size

    inv_a = modinv(a, deck_size)
    inv_b = (-b * inv_a) % deck_size

    final_a = pow(inv_a, shuffles, deck_size)
    final_b = (inv_b * (1 - final_a) * modinv((1 - inv_a) % deck_size, deck_size)) % deck_size

    answer = (final_a * target_position + final_b) % deck_size
    print(answer)
    AOC.submit_answer(answer)


if __name__ == "__main__":
    solve()
