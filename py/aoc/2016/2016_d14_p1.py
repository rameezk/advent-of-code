from aoc.helper import AOC
import hashlib
import re


@AOC.puzzle(2016, 14, 1)
def solve():
    salt = AOC.get_data().strip()

#     salt = """abc"""

    def get_hash(index):
        return hashlib.md5(f"{salt}{index}".encode()).hexdigest()

    def find_triple(hash_str):
        for i in range(len(hash_str) - 2):
            if hash_str[i] == hash_str[i+1] == hash_str[i+2]:
                return hash_str[i]
        return None

    def has_quintuple(hash_str, char):
        return char * 5 in hash_str

    keys_found = []
    index = 0

    while len(keys_found) < 64:
        current_hash = get_hash(index)
        triple_char = find_triple(current_hash)

        if triple_char:
            for j in range(index + 1, index + 1001):
                next_hash = get_hash(j)
                if has_quintuple(next_hash, triple_char):
                    keys_found.append(index)
                    print(f"Key {len(keys_found)}: index {index}")
                    break

        index += 1

    result = keys_found[63]
    print(f"64th key at index: {result}")
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
