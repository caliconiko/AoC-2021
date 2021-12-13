import numpy as np

with open("day13.txt") as f:
    raw = f.read()
    lines = [line.strip() for line in raw.strip().split("\n")]

def print_paper(pa):
    for j in range(len(pa[0])):
        for i in range(len(pa)):
            p = pa[i][j]
            if p >= 1:
                print("#", end="")
            else:
                print(".", end="")
        print()

def part1():
    sections = raw.split("\n\n")
    points = [[int(n) for n in l.split(",")] for l in sections[0].splitlines()]
    instructions = [[l.split()[2].split("=")[0], int(l.split()[2].split("=")[1])] for l in sections[1].splitlines()]
    print(instructions)

    # print(points)

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    maxx, maxy = np.max(xs), np.max(ys)

    paper = np.zeros((maxx+1, maxy+1))

    for p in points:
        paper[p[0]][p[1]] = 1

    print((maxx+1, maxy+1))

    for axis, pos in instructions[0:1]:
        if axis=="x":

            half = paper[pos+1::, ::]
            flip = half[::-1,::]

            otherside = paper[:pos:, ::]

            if otherside.shape[0] >= flip.shape[0]:
                otherside[otherside.shape[0]-flip.shape[0]:,:] += flip
                paper = otherside
            else:
                flip[flip.shape[0]-otherside.shape[0]:,:]+=otherside
                paper = flip

        else:
            half = paper[::, pos+1::]
            flip = half[::, ::-1]

            otherside = paper[::, :pos:]

            if otherside.shape[1] >= flip.shape[1]:
                otherside[:,otherside.shape[1]-flip.shape[1]:] += flip
                paper = otherside
            else:
                flip[:,flip.shape[1]-otherside.shape[1]:]+=otherside
                paper = flip

    print(np.sum(paper>=1))


def part2():
    ...
    sections = raw.split("\n\n")
    points = [[int(n) for n in l.split(",")] for l in sections[0].splitlines()]
    instructions = [[l.split()[2].split("=")[0], int(l.split()[2].split("=")[1])] for l in sections[1].splitlines()]
    print(instructions)

    # print(points)

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    maxx, maxy = np.max(xs), np.max(ys)

    paper = np.zeros((maxx+1, maxy+1))

    for p in points:
        paper[p[0]][p[1]] = 1

    print((maxx+1, maxy+1))

    for axis, pos in instructions:
        if axis=="x":

            half = paper[pos+1::, ::]
            flip = half[::-1,::]

            otherside = paper[:pos:, ::]

            if otherside.shape[0] >= flip.shape[0]:
                otherside[otherside.shape[0]-flip.shape[0]:,:] += flip
                paper = otherside
            else:
                flip[flip.shape[0]-otherside.shape[0]:,:]+=otherside
                paper = flip

        else:
            half = paper[::, pos+1::]
            flip = half[::, ::-1]

            otherside = paper[::, :pos:]

            if otherside.shape[1] >= flip.shape[1]:
                otherside[:,otherside.shape[1]-flip.shape[1]:] += flip
                paper = otherside
            else:
                flip[:,flip.shape[1]-otherside.shape[1]:]+=otherside
                paper = flip

    print_paper(paper)

part1()
part2()