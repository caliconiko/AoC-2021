import numpy as np
from collections import Counter, defaultdict

with open("day14.txt") as f:
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
    N = 'n'
    sections = raw.split("\n\n")

    template = sections[0].strip()

    rules = {l.split(" -> ")[0]:l.split(" -> ")[1] for l in sections[1].splitlines()}

    tail = template[-1]

    pairs = defaultdict(int)

    for i in range(len(template)-1):
        pairs[template[i:i+2]] += 1

    print(pairs)

    for _ in range(40):
        new_pairs = pairs.copy()
        for pair, number in pairs.items():
            if number>0:
                if pair in rules.keys():
                    new_element = rules[pair]

                    new_pairs[pair[0]+new_element+N]+=number
                    new_pairs[new_element+pair[1]+N]+=number
                    new_pairs[pair]=0
                    # print(f"{new_pairs} \n{pair}")    
                else:
                    new_pairs[pair+N] = number

        new_new_pairs = new_pairs.copy()
        for n_pair, n_number in new_pairs.items():
            if n_pair[-1]==N:
                new_new_pairs[n_pair[:2]]+=n_number
                new_new_pairs[n_pair]=0

        pairs = new_new_pairs
        # print(f"{new_pairs}")  
        # print("-----")

    count = defaultdict(int)
    for pair, number in pairs.items():
        count[pair[0]]+=number
    count[tail]+=1

    total = 0
    for c in count.values():
        total+=c
    total+=1

    print(count)
    print(total)

    count_numbers = list(count.values())
    count_numbers.sort()

    print(count_numbers[-1]-count_numbers[0])

part1()
part2()