import numpy as np
from collections import Counter

with open("day14t.txt") as f:
    raw = f.read()
    lines = [line.strip() for line in raw.strip().split("\n")]

def part1():
    sections = raw.split("\n\n")

    template = sections[0].strip()

    rules = {l.split(" -> ")[0]:l.split(" -> ")[1] for l in sections[1].splitlines()}

    polymer = template
    
    for _ in range(10):
        insert = list(polymer)
        for i in range(len(polymer)-1):
            pair = polymer[i:i+2]
            if pair in rules.keys():
                insert[i]+=rules[pair]
        polymer = "".join(insert)
        # print(polymer)

    count = Counter(polymer).most_common()

    print(count[0][1]-count[-1][1])

def part2():
    ...
    sections = raw.split("\n\n")

    template = sections[0].strip()

    rules = {l.split(" -> ")[0]:l.split(" -> ")[1] for l in sections[1].splitlines()}

    polymer = template

part1()