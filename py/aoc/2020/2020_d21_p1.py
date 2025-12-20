from aoc.helper import AOC

@AOC.puzzle(2020, 21, 1)
def solve():
    data = AOC.get_data().strip().splitlines()

#     data = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
# trh fvjkl sbzzf mxmxvkd (contains dairy)
# sqjhc fvjkl (contains soy)
# sqjhc mxmxvkd sbzzf (contains fish)""".splitlines()

    foods = []
    all_ingredients = set()
    all_allergens = set()

    for line in data:
        parts = line.strip().rstrip(')').split(' (contains ')
        ingredients = set(parts[0].split())
        allergens = set()
        if len(parts) > 1:
            allergens = set(parts[1].split(', '))

        foods.append((ingredients, allergens))
        all_ingredients.update(ingredients)
        all_allergens.update(allergens)

    possible_ingredients = {}
    for allergen in all_allergens:
        possible_ingredients[allergen] = set(all_ingredients)

        for ingredients, allergens in foods:
            if allergen in allergens:
                possible_ingredients[allergen] &= ingredients

    ingredients_with_allergens = set()
    for allergen, ingredients in possible_ingredients.items():
        ingredients_with_allergens.update(ingredients)

    safe_ingredients = all_ingredients - ingredients_with_allergens

    count = 0
    for ingredients, allergens in foods:
        for ingredient in safe_ingredients:
            if ingredient in ingredients:
                count += 1

    answer = count
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
