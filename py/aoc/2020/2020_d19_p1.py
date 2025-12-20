from aoc.helper import AOC

@AOC.puzzle(2020, 19, 1)
def solve():
    data = AOC.get_data().strip()

#     data = """0: 4 1 5
# 1: 2 3 | 3 2
# 2: 4 4 | 5 5
# 3: 4 5 | 5 4
# 4: "a"
# 5: "b"
#
# ababbb
# bababa
# abbbab
# aaabbb
# aaaabbb"""

    parts = data.split("\n\n")
    rules_text = parts[0]
    messages = parts[1].split("\n")

    rules = {}
    for line in rules_text.split("\n"):
        rule_id, rule_def = line.split(": ")
        rule_id = int(rule_id)
        if '"' in rule_def:
            rules[rule_id] = rule_def.strip('"')
        else:
            options = []
            for option in rule_def.split(" | "):
                options.append([int(x) for x in option.split()])
            rules[rule_id] = options

    def match(rule_id, text, pos):
        if pos >= len(text):
            return []

        rule = rules[rule_id]

        if isinstance(rule, str):
            if text[pos] == rule:
                return [pos + 1]
            else:
                return []

        valid_positions = []
        for option in rule:
            current_positions = [pos]
            for sub_rule in option:
                next_positions = []
                for p in current_positions:
                    next_positions.extend(match(sub_rule, text, p))
                current_positions = next_positions
                if not current_positions:
                    break
            valid_positions.extend(current_positions)

        return valid_positions

    count = 0
    for message in messages:
        positions = match(0, message, 0)
        if len(message) in positions:
            count += 1

    print(f"Count: {count}")
    AOC.submit_answer(count)

if __name__ == "__main__":
    solve()
