from aoc.helper import AOC


@AOC.puzzle(year=2024, day=5, part=1)
def solve():
    data = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47"""

    data = AOC.get_data()

    rules, updates = data.split("\n\n")
    rules = parse_rules(rules)
    updates = parse_updates(updates)

    result = 0
    for update in updates:
        if is_valid_update(update, rules):
            result += update[len(update) // 2]

    print(result)
    AOC.submit_answer(result)


def is_valid_update(update, rules):
    seen = set(update)
    for before, after in rules:
        if before in seen and after in seen:
            before_i = update.index(before)
            after_i = update.index(after)
            if before_i > after_i:
                return False
    return True


def parse_rules(rules):
    parsed_rules = []
    for rule in rules.splitlines():
        before, after = map(int, rule.split("|"))
        parsed_rules.append((before, after))
    return parsed_rules


def parse_updates(updates):
    parsed_updates = []
    for update in updates.splitlines():
        pages = list(map(int, update.split(",")))
        parsed_updates.append(pages)
    return parsed_updates


if __name__ == "__main__":
    solve()
