import numpy as np

with open("day12tttt.txt") as f:
    raw = f.read()
    lines = [line.strip() for line in raw.strip().split("\n")]

def part1():
    connections = {}
    print(lines)
    for l in lines:
        splitted = l.split("-")
        first = splitted[0]
        second = splitted[1]

        if first in connections.keys():
            connections[first].append(second)
        else:
            connections[first] = [second]

        if second in connections.keys():
            connections[second].append(first)
        else:
            connections[second] = [first]

    print(connections)
    all_paths_just_for_funsies = []



    def find_paths(so_far, next_cave):
        nonlocal connections
        nonlocal all_paths_just_for_funsies
        valid_next = []

        if next_cave=="end":
            all_paths_just_for_funsies.append(so_far)
            return 1

        for maybe in connections[next_cave]:
            if maybe == "start":
                continue
            if maybe.upper()==maybe:
                valid_next.append(maybe)
            if maybe.lower()==maybe:
                if maybe not in so_far:
                    valid_next.append(maybe)
        
        if len(valid_next)==0:
            return 0

        total_paths = 0

        for v in valid_next:
            total_paths+=find_paths(so_far+[next_cave], v)

        return total_paths
        ...
    total_of_all_of_the_possible_dingdang_paths = 0
    for after_start in connections["start"]:
        total_of_all_of_the_possible_dingdang_paths += find_paths([after_start], after_start)

    print(total_of_all_of_the_possible_dingdang_paths)


def part2():
    connections = {}
    print(lines)
    for l in lines:
        splitted = l.split("-")
        first = splitted[0]
        second = splitted[1]

        if first in connections.keys():
            connections[first].append(second)
        else:
            connections[first] = [second]

        if second in connections.keys():
            connections[second].append(first)
        else:
            connections[second] = [first]

    print(connections)
    all_paths = set()

    smol_caves = [cave for cave in connections.keys() if cave.lower()==cave and cave not in ["start", "end"]]
    print(smol_caves)

    def find_paths(so_far, next_cave, smol):
        nonlocal connections
        nonlocal all_paths
        valid_next = []

        if next_cave=="end":
            all_paths.add(tuple(so_far))
            return 1

        for maybe in connections[next_cave]:
            if maybe == "start":
                continue
            if maybe.upper()==maybe:
                valid_next.append(maybe)
            if maybe.lower()==maybe:
                if maybe not in so_far:
                    valid_next.append(maybe)
                elif maybe==smol:
                    if so_far.count(smol)<2:
                        valid_next.append(maybe)
        
        if len(valid_next)==0:
            return 0

        total_paths = 0

        for v in valid_next:
            total_paths+=find_paths(so_far+[next_cave], v, smol)

        return total_paths
        ...
    total_of_all_of_the_possible_dingdang_paths = 0
    for after_start in connections["start"]:
        for smol in smol_caves:
            total_of_all_of_the_possible_dingdang_paths += find_paths(["start"], after_start, smol)

    print(total_of_all_of_the_possible_dingdang_paths)
    print(len(all_paths))
    # print(all_paths)
    ...

part1()