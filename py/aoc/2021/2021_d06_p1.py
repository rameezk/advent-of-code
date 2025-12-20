from aoc.helper import AOC

@AOC.puzzle(2021, 6, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """3,4,3,1,2"""

    fish = list(map(int, data.split(',')))

    for day in range(80):
        new_fish = []
        for i in range(len(fish)):
            if fish[i] == 0:
                fish[i] = 6
                new_fish.append(8)
            else:
                fish[i] -= 1
        fish.extend(new_fish)

    answer = len(fish)

    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
