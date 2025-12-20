from aoc.helper import AOC

@AOC.puzzle(2020, 15, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """0,3,6"""

    starting_numbers = list(map(int, data.split(',')))

    memory = {}

    for i in range(len(starting_numbers) - 1):
        memory[starting_numbers[i]] = i + 1

    last_spoken = starting_numbers[-1]

    target_turn = 2020

    for turn in range(len(starting_numbers) + 1, target_turn + 1):
        if last_spoken in memory:
            next_number = turn - 1 - memory[last_spoken]
        else:
            next_number = 0

        memory[last_spoken] = turn - 1
        last_spoken = next_number

    answer = last_spoken

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
