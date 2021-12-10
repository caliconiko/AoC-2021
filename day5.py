import numpy as np

with open("day5.txt") as f:
    raw = f.read()
    lines = [line.strip() for line in raw.strip().split("\n")]

def part1():
    pass
    pairs = [[[int(n) for n in p.split(",")] for p in line.split(" -> ")] for line in lines]

    print(pairs)
    
    right_pairs = [pair for pair in pairs if (pair[0][0] == pair[1][0]) or (pair[0][1] == pair[1][1])]
    print(right_pairs)

    xs = [p[0] for pair in right_pairs for p in pair]
    ys = [p[1] for pair in right_pairs for p in pair]
    max_x = np.max(xs)
    max_y = np.max(ys)
    print((max_x, max_y))

    world = np.zeros((max_x+2, max_y+2))
    print(world)

    for pair in right_pairs:
        yp = (pair[0][1], pair[1][1])
        for y in range(min(yp), max(yp)+1):
            xp = (pair[0][0], pair[1][0])
            for x in range(min(xp), max(xp)+1):
                world[y,x]+=1

    print(len(np.where(world>1)[0]))

def part2():
    pass
    pairs = [[[int(n) for n in p.split(",")] for p in line.split(" -> ")] for line in lines]

    print(pairs)
    
    right_pairs = [pair for pair in pairs if (pair[0][0] == pair[1][0]) or (pair[0][1] == pair[1][1])]
    diag_pairs = [pair for pair in pairs if not ((pair[0][0] == pair[1][0]) or (pair[0][1] == pair[1][1]))]
    print(right_pairs)

    xs = [p[0] for pair in pairs for p in pair]
    ys = [p[1] for pair in pairs for p in pair]
    max_x = np.max(xs)
    max_y = np.max(ys)
    print((max_x, max_y))

    world = np.zeros((max_y+1, max_x+1))

    for pair in right_pairs:
        yp = (pair[0][1], pair[1][1])
        for y in range(min(yp), max(yp)+1):
            xp = (pair[0][0], pair[1][0])
            for x in range(min(xp), max(xp)+1):
                world[y,x]+=1

    print((max_x, max_y))
    for pair in diag_pairs:
        sx = pair[1][0] - pair[0][0]
        sy = pair[1][1] - pair[0][1]

        [x, y] = pair[0]
        for _ in range(abs(sx)+1):
            world[y,x]+=1
            x+=np.sign(sx)
            y+=np.sign(sy)


    print(len(np.where(world>1)[0]))


part2()