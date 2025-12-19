from aoc.helper import AOC
from collections import Counter


@AOC.puzzle(2016, 4, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """aaaaa-bbb-z-y-x-123[abxyz]
# a-b-c-d-e-f-g-h-987[abcde]
# not-a-real-room-404[oarel]
# totally-real-room-200[decoy]""".strip().splitlines()

    total = 0

    for line in data:
        parts = line.rsplit('-', 1)
        encrypted_name = parts[0].replace('-', '')
        sector_and_checksum = parts[1]

        sector_id = int(sector_and_checksum.split('[')[0])
        checksum = sector_and_checksum.split('[')[1].rstrip(']')

        letter_counts = Counter(encrypted_name)
        sorted_letters = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))
        expected_checksum = ''.join([letter for letter, count in sorted_letters[:5]])

        if checksum == expected_checksum:
            total += sector_id

    print(total)
    AOC.submit_answer(total)


if __name__ == "__main__":
    solve()
