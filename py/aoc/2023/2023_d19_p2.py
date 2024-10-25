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


def count(rule_engine, ranges, workflow_id) -> int:
    if workflow_id == "R":
        return 0

    if workflow_id == "A":
        product = 1
        for low, high in ranges.values():
            product *= high - low + 1
        return product

    rules, fallback = rule_engine[workflow_id]

    T = 0

    for rule in rules:
        key, n = re.split(r"[<>]", rule[0])
        n = int(n)
        target = rule[1]

        low, high = ranges[key]
        if "<" in rule[0]:
            t = (low, n - 1)
            f = (n, high)
        else:
            t = (n + 1, high)
            f = (low, n)

        if t[0] <= t[1]:
            copy = dict(ranges)
            copy[key] = t
            T += count(rule_engine, copy, target)

        if f[0] <= f[1]:
            ranges = dict(ranges)
            ranges[key] = f
        else:
            break
    else:
        T += count(rule_engine, ranges, fallback)

    return T


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
    C = count(rule_engine, {key: (1, 4000) for key in "xmas"}, "in")
    print(C)
    # submit_answer(2023, 19, 2, C)


if __name__ == "__main__":
    run()
