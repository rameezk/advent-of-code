from aoc.helper import AOC

@AOC.puzzle(2020, 21, 2)
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

    allergen_to_ingredient = {}
    while possible_ingredients:
        for allergen, ingredients in possible_ingredients.items():
            if len(ingredients) == 1:
                ingredient = list(ingredients)[0]
                allergen_to_ingredient[allergen] = ingredient

                del possible_ingredients[allergen]

                for other_allergen in possible_ingredients:
                    possible_ingredients[other_allergen].discard(ingredient)
                break

    sorted_allergens = sorted(allergen_to_ingredient.keys())
    dangerous_ingredients = [allergen_to_ingredient[allergen] for allergen in sorted_allergens]

    answer = ','.join(dangerous_ingredients)
    AOC.submit_answer(answer)

if __name__ == "__main__":
    solve()
