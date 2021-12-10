import numpy as np

with open("day9.txt") as f:
    raw = f.read()
    lines = [line.strip() for line in raw.strip().split("\n")]

def part1():
    floor = [[int(n) for n in l] for l in lines]

    tot = 0

    def get_floor(i,j):
        if i<0 or j<0:
            return 10
        if i>=len(floor) or j>=len(floor[0]):
            return 10
        return floor[i][j]

    print(len(floor))
    print(len(floor[0]))

    for i, l in enumerate(floor):
        # y
        for j, n in enumerate(l):
            # x
            up = get_floor(i-1, j)
            down = get_floor(i+1, j)
            left = get_floor(i, j-1)
            right = get_floor(i, j+1)
            

            if n<down and n<up and n<left and n<right:
                risk = n+1
                print(n)
                tot+=risk

    print(tot)
            

def part2():
    floor = [[int(n) for n in l] for l in lines]

    sizes = []

    def get_floor(i,j):
        if i<0 or j<0:
            return 10
        if i>=len(floor) or j>=len(floor[0]):
            return 10
        return floor[i][j]

    print(len(floor))
    print(len(floor[0]))

    current_basin = set()

    def get_floor_and_pos(i, j):
        return (get_floor(i,j), (i,j))

    def check_basin(i, j):
        nonlocal current_basin

        b = get_floor(i, j)
        up = get_floor_and_pos(i-1, j)
        down = get_floor_and_pos(i+1, j)
        left = get_floor_and_pos(i, j-1)
        right = get_floor_and_pos(i, j+1)
        
        to_add = set()
        next_add = set()

        for n, d in [up, down, left, right]:
            if n>b and n<9 and (d not in current_basin):
                to_add.add(n)
                next_add.add(d)

        current_basin|=next_add

        for ni, nj in next_add:
            check_basin(ni, nj)


    for i, l in enumerate(floor):
        # y
        for j, n in enumerate(l):
            # x
            up = get_floor(i-1, j)
            down = get_floor(i+1, j)
            left = get_floor(i, j-1)
            right = get_floor(i, j+1)
            

            if n<down and n<up and n<left and n<right:
                current_basin.add((i,j))
                check_basin(i, j)
                sizes.append(len(current_basin))
                current_basin.clear()
    sizes.sort()
    print(sizes)
    print(sizes[-1]*sizes[-2]*sizes[-3])

part2()