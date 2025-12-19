from aoc.helper import AOC
import re


@AOC.puzzle(2015, 15, 2)
def solve():
    # sample_data = """Butterscotch: capacity -1, durability -2, flavor 6, texture 3, calories 8
# Cinnamon: capacity 2, durability 3, flavor -2, texture -1, calories 3"""

    # data = sample_data.strip()
    data = AOC.get_data().strip()

    ingredients = {}
    for line in data.split('\n'):
        match = re.match(r'(\w+): capacity (-?\d+), durability (-?\d+), flavor (-?\d+), texture (-?\d+), calories (-?\d+)', line)
        if match:
            name = match.group(1)
            capacity = int(match.group(2))
            durability = int(match.group(3))
            flavor = int(match.group(4))
            texture = int(match.group(5))
            calories = int(match.group(6))
            ingredients[name] = {
                'capacity': capacity,
                'durability': durability,
                'flavor': flavor,
                'texture': texture,
                'calories': calories
            }

    ingredient_names = list(ingredients.keys())
    n = len(ingredient_names)

    def calculate_score(amounts):
        capacity = sum(amounts[i] * ingredients[ingredient_names[i]]['capacity'] for i in range(n))
        durability = sum(amounts[i] * ingredients[ingredient_names[i]]['durability'] for i in range(n))
        flavor = sum(amounts[i] * ingredients[ingredient_names[i]]['flavor'] for i in range(n))
        texture = sum(amounts[i] * ingredients[ingredient_names[i]]['texture'] for i in range(n))

        capacity = max(0, capacity)
        durability = max(0, durability)
        flavor = max(0, flavor)
        texture = max(0, texture)

        return capacity * durability * flavor * texture

    def calculate_calories(amounts):
        return sum(amounts[i] * ingredients[ingredient_names[i]]['calories'] for i in range(n))

    def generate_combinations(total, num_ingredients):
        if num_ingredients == 1:
            yield [total]
        else:
            for i in range(total + 1):
                for rest in generate_combinations(total - i, num_ingredients - 1):
                    yield [i] + rest

    max_score = 0
    for amounts in generate_combinations(100, n):
        if calculate_calories(amounts) == 500:
            score = calculate_score(amounts)
            max_score = max(max_score, score)

    result = max_score
    AOC.submit_answer(result)


if __name__ == "__main__":
    solve()
