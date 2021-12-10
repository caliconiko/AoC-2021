
with open("day1") as f:
    day1_part1 = f.readlines()

def part1():
    total = 0
    for i, _ in enumerate(day1_part1):
        if i!=0:
            if int(day1_part1[i]) > int(day1_part1[i-1]):
                total+=1
    return total

def part2():
    total=0
    for i, _ in enumerate(day1_part1):
        if i>2:
            first = int(day1_part1[i]) + int(day1_part1[i-1]) + int(day1_part1[i-2])
            second = int(day1_part1[i-1]) + int(day1_part1[i-2]) + int(day1_part1[i-3])
            if first>second:
                total+=1
    return total

print(part2())