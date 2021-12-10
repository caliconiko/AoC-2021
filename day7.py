import numpy as np
import cProfile
import time

with open("day7.txt") as f:
    raw = f.read()
    lines = [line.strip() for line in raw.strip().split("\n")]

def part1():
    crabs = [int(n) for n in lines[0].split(",")]
    crabs_np = np.array(crabs)
    m = np.max(crabs)

    a = np.average(crabs)
    
    sus = []
    fus = []
    iss = []

    for i in range(m+1):
        fu = abs(crabs_np-i)
        fus.append(fu)

        su = np.sum(fu)
        sus.append(su)

        iss.append(i)

    print(np.min(sus))
    print(np.array(iss)[np.where(np.array(sus)==np.min(sus))])


def part2():
    crabs = [int(n) for n in lines[0].split(",")]
    crabs_np = np.array(crabs)
    m = np.max(crabs)

    a = np.average(crabs)
    
    sus = []
    fus = []
    iss = []

    for i in range(m+1):
        fuu = abs(crabs_np-i)
        fu = (fuu*(fuu+1))/2

        fus.append(fu)

        su = np.sum(fu)
        sus.append(su)

        iss.append(i)

    print(np.min(sus))
    print(np.array(iss)[np.where(np.array(sus)==np.min(sus))])

def part2o():
    crabs = [int(n) for n in lines[0].split(",")]
    crabs_np = np.array(crabs)
    m = np.max(crabs)

    sus = []

    for i in range(m+1):
        fuu = abs(crabs_np-i)
        fu = (fuu*(fuu+1))/2

        su = np.sum(fu)
        sus.append(su)

    print(np.min(sus))

part2()

cProfile.runctx(
    "part2o()",
    globals(),
    locals(),
    sort="tottime",
)

t1 = time.time()
part2o()
t2 = time.time()

print(t2-t1)