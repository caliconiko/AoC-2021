import numpy as np

with open("day20t.txt") as f:
    raw = f.read()
    lines = [line.strip() for line in raw.strip().split("\n")]

def expand(a:np.array):
    return np.pad(a, 1, mode="constant", constant_values=0)

def part1():
    ...
    sections = raw.split("\n\n")
    print(sections[0])

    algorithm = tuple(int(n) for n in sections[0].replace("\n", "").replace("#", "1").replace(".", "0"))

    image = np.array([[int(n) for n in l]for l in sections[1].replace("#", "1").replace(".", "0").splitlines()])

    print(image)
    print(expand(image))
    print(algorithm)


part1()