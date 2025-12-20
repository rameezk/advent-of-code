from aoc.helper import AOC


@AOC.puzzle(2018, 14, 2)
def solve():
    data = AOC.get_data().strip()

#     data = """51589"""
#     data = """01245"""
#     data = """92510"""
#     data = """59414"""

    target_seq = [int(c) for c in data]
    target_len = len(target_seq)

    recipes = [3, 7]
    elf1 = 0
    elf2 = 1

    while True:
        sum_score = recipes[elf1] + recipes[elf2]

        if sum_score >= 10:
            recipes.append(1)
            if len(recipes) >= target_len and recipes[-target_len:] == target_seq:
                result = len(recipes) - target_len
                print(result)
                AOC.submit_answer(result)
                return
            recipes.append(sum_score - 10)
            if len(recipes) >= target_len and recipes[-target_len:] == target_seq:
                result = len(recipes) - target_len
                print(result)
                AOC.submit_answer(result)
                return
        else:
            recipes.append(sum_score)
            if len(recipes) >= target_len and recipes[-target_len:] == target_seq:
                result = len(recipes) - target_len
                print(result)
                AOC.submit_answer(result)
                return

        elf1 = (elf1 + 1 + recipes[elf1]) % len(recipes)
        elf2 = (elf2 + 1 + recipes[elf2]) % len(recipes)


if __name__ == "__main__":
    solve()
