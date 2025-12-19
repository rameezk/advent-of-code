from aoc.helper import AOC

@AOC.puzzle(2017, 4, 2)
def solve():
    data = AOC.get_data().strip()

    sample = """abcde fghij
abcde xyz ecdab
a ab abc abd abf abj
iiii oiii ooii oooi oooo
oiii ioii iioi iiio"""

    lines = sample.split('\n')

    valid_count = 0
    for line in lines:
        words = line.split()
        sorted_words = [''.join(sorted(word)) for word in words]
        if len(sorted_words) == len(set(sorted_words)):
            valid_count += 1

    print(f"Sample result: {valid_count}")

    lines = data.split('\n')

    valid_count = 0
    for line in lines:
        words = line.split()
        sorted_words = [''.join(sorted(word)) for word in words]
        if len(sorted_words) == len(set(sorted_words)):
            valid_count += 1

    answer = valid_count
    print(f"Answer: {answer}")
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
