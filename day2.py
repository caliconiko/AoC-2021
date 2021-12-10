with open("day2.txt") as f:
    data = f.readlines()


def part1():
    hor = 0
    dep = 0
    print(data)
    for line in data:
        splitted = line.split(" ")
        command =splitted[0]
        num = int(splitted[1])
        match command:
            case "forward":
                hor += num
            case "up":
                dep -= num
            case "down":
                dep += num
    return hor*dep

def part2():
    hor = 0
    dep = 0
    aim = 0
    for line in data:
        splitted = line.split(" ")
        command =splitted[0]
        num = int(splitted[1])
        match command:
            case "forward":
                hor += num
                dep += aim*num
            case "up":
                aim -= num
            case "down":
                aim += num
    return dep*hor
print(part2())