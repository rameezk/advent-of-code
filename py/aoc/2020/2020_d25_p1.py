from aoc.helper import AOC

@AOC.puzzle(2020, 25, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """5764801
# 17807724""".splitlines()

    card_public_key = int(data[0])
    door_public_key = int(data[1])

    def transform(subject_number, loop_size):
        value = 1
        for _ in range(loop_size):
            value = (value * subject_number) % 20201227
        return value

    def find_loop_size(public_key):
        value = 1
        loop_size = 0
        while value != public_key:
            value = (value * 7) % 20201227
            loop_size += 1
        return loop_size

    card_loop_size = find_loop_size(card_public_key)
    door_loop_size = find_loop_size(door_public_key)

    encryption_key = transform(door_public_key, card_loop_size)

    answer = encryption_key

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
