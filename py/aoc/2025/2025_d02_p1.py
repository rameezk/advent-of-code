from aoc.helper import AOC


@AOC.puzzle(2025, 2, 1)
def solve():
    data = AOC.get_data()

    # data = "11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"

    total = 0
    for line in data.strip().split(","):
        start, end = line.split("-")
        invalid_ids = list(find_invalid_ids(int(start), int(end)))
        total += sum(invalid_ids)

    print(total)
    AOC.submit_answer(total)

def is_repeated_sequence(n):
    s = str(n)
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return s[:mid] == s[mid:]

def find_invalid_ids(start, end):
    for n in range(start, end+1):
        if is_repeated_sequence(n):
            yield n

if __name__ == "__main__":
    solve()
