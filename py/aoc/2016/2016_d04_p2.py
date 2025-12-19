from aoc.helper import AOC
from collections import Counter


@AOC.puzzle(2016, 4, 2)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """qzmt-zixmtkozy-ivhz-343""".strip().splitlines()

    for line in data:
        parts = line.rsplit('-', 1)
        encrypted_name = parts[0]
        sector_and_checksum = parts[1]

        sector_id = int(sector_and_checksum.split('[')[0])
        checksum = sector_and_checksum.split('[')[1].rstrip(']')

        letter_counts = Counter(encrypted_name.replace('-', ''))
        sorted_letters = sorted(letter_counts.items(), key=lambda x: (-x[1], x[0]))
        expected_checksum = ''.join([letter for letter, count in sorted_letters[:5]])

        if checksum == expected_checksum:
            decrypted = ''
            for char in encrypted_name:
                if char == '-':
                    decrypted += ' '
                else:
                    shifted = ord(char) - ord('a')
                    shifted = (shifted + sector_id) % 26
                    decrypted += chr(shifted + ord('a'))

            if 'north' in decrypted and 'pole' in decrypted:
                print(f"{decrypted}: {sector_id}")
                AOC.submit_answer(sector_id)


if __name__ == "__main__":
    solve()
