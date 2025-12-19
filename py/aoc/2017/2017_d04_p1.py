from aoc.helper import AOC

@AOC.puzzle(2017, 4, 1)
def solve():
    data = AOC.get_data().strip()

    sample = """aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa"""

    lines = sample.split('\n')

    valid_count = 0
    for line in lines:
        words = line.split()
        if len(words) == len(set(words)):
            valid_count += 1

    print(f"Sample result: {valid_count}")

    lines = data.split('\n')

    valid_count = 0
    for line in lines:
        words = line.split()
        if len(words) == len(set(words)):
            valid_count += 1

    answer = valid_count
    print(f"Answer: {answer}")
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
