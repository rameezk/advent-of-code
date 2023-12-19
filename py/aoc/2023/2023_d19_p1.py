from aoc.helper import download_input, submit_answer
from aoc.util import benchmark
import re


def build_rule_engine(workflows):
    rule_engine = {}
    for workflow in workflows.splitlines():
        w_id, rules = workflow.split("{")
        rules = rules[:-1]
        rules = rules.split(",")

        prs = []
        for rule in rules[:-1]:
            prs.append(rule.split(":"))

        rule_engine[w_id] = (prs, rules[-1])
    return rule_engine


def evaluate(rule_engine, x, m, a, s) -> bool:
    rule_set = rule_engine["in"]

    while True:
        rules, fallback = rule_set

        for rule in rules:
            r = eval(rule[0])

            if r:
                if rule[1] == "A":
                    return True
                if rule[1] == "R":
                    return False

                rule_set = rule_engine[rule[1]]
                break
        else:
            if fallback == "A":
                return True
            if fallback == "R":
                return False

            rule_set = rule_engine[fallback]


@benchmark
def run():
    download_input(2023, 19)

    data = """
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
    """.strip()

    with open("./2023_d19.txt") as f:
        data = f.read().strip()

    workflows, ratings = data.split("\n\n")

    # build rule engine
    rule_engine = build_rule_engine(workflows)
    S = 0
    for rating in ratings.splitlines():
        x, m, a, s = map(int, re.findall(r"\d+", rating))
        is_accepted = evaluate(rule_engine, x, m, a, s)
        if is_accepted:
            S += sum([x, m, a, s])
    print(S)
    # submit_answer(2023, 19, 1, S)


if __name__ == "__main__":
    run()
