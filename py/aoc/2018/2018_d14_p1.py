from aoc.helper import AOC


@AOC.puzzle(2018, 14, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """9"""
#     data = """5"""
#     data = """18"""
#     data = """2018"""

    target = int(data)

    recipes = [3, 7]
    elf1 = 0
    elf2 = 1

    while len(recipes) < target + 10:
        sum_score = recipes[elf1] + recipes[elf2]

        if sum_score >= 10:
            recipes.append(1)
            recipes.append(sum_score - 10)
        else:
            recipes.append(sum_score)

        elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
        elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)

    result = ''.join(str(r) for r in recipes[target:target+10])
    print(result)
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
