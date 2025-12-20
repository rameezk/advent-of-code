from aoc.helper import AOC

@AOC.puzzle(2020, 19, 2)
def solve():
    data = AOC.get_data().strip()

#     data = """42: 9 14 | 10 1
# 9: 14 27 | 1 26
# 10: 23 14 | 28 1
# 1: "a"
# 11: 42 31
# 5: 1 14 | 15 1
# 19: 14 1 | 14 14
# 12: 24 14 | 19 1
# 16: 15 1 | 14 14
# 31: 14 17 | 1 13
# 6: 14 14 | 1 14
# 2: 1 24 | 14 4
# 0: 8 11
# 13: 14 3 | 1 12
# 15: 1 | 14
# 17: 14 2 | 1 7
# 23: 25 1 | 22 14
# 28: 16 1
# 4: 1 1
# 20: 14 14 | 1 15
# 3: 5 14 | 16 1
# 27: 1 6 | 14 18
# 14: "b"
# 21: 14 1 | 1 14
# 25: 1 1 | 1 14
# 22: 14 14
# 8: 42
# 26: 14 22 | 1 20
# 18: 15 15
# 7: 14 5 | 1 21
# 24: 14 1
#
# abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
# bbabbbbaabaabba
# babbbbaabbbbbabbbbbbaabaaabaaa
# aaabbbbbbaaaabaababaabababbabaaabbababababaaa
# bbbbbbbaaaabbbbaaabbabaaa
# bbbababbbbaaaaaaaabbababaaababaabab
# ababaaaaaabaaab
# ababaaaaabbbaba
# baabbaaaabbaaaababbaababb
# abbbbabbbbaaaababbbbbbaaaababb
# aaaaabbaabaaaaababaa
# aaaabbaaaabbaaa
# aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
# babaaabbbaaabaababbaabababaaab
# aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""

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

    rules[8] = [[42], [42, 8]]
    rules[11] = [[42, 31], [42, 11, 31]]

    memo = {}

    def match(rule_id, text, pos, depth=0):
        if depth > 100:
            return []

        if pos >= len(text):
            return []

        cache_key = (rule_id, pos, depth)
        if cache_key in memo:
            return memo[cache_key]

        rule = rules[rule_id]

        if isinstance(rule, str):
            if text[pos] == rule:
                result = [pos + 1]
            else:
                result = []
            memo[cache_key] = result
            return result

        valid_positions = []
        for option in rule:
            current_positions = [pos]
            for sub_rule in option:
                next_positions = []
                for p in current_positions:
                    next_positions.extend(match(sub_rule, text, p, depth + 1))
                current_positions = next_positions
                if not current_positions:
                    break
            valid_positions.extend(current_positions)

        memo[cache_key] = valid_positions
        return valid_positions

    count = 0
    for message in messages:
        memo.clear()
        positions = match(0, message, 0)
        if len(message) in positions:
            count += 1

    print(f"Count: {count}")
    AOC.submit_answer(count)

if __name__ == "__main__":
    solve()
