import numpy as np

with open("day3.txt") as f:
    data = [line.strip() for line in f.readlines()]

def part1():
    bits = [""]*len(data[0])
    bit_result = ""
    for line in data:
        for i, n in enumerate(line):
            bits[i]+=n

    totals = [str(int(np.sum([int(i) for i in b])>np.ceil(len(data)/2))) for b in bits]
    not_totals = [str(int(not bool(int(i)))) for i in totals]

    gamma = int("".join(totals), 2)
    epsilon = int("".join(not_totals), 2)

    return gamma*epsilon

def part2():
    
    o2 = data.copy()

    i=0
    while len(o2)>1:
        su = 0
        for d in o2:
            if d[i] == "1":
                su+=1
            else:
                su-=1

        target=str(int(su>=0))
        print(o2)
        print(f"{su} {target}")
        o2 = [o for o in o2 if o[i]==target]
        i+=1

    o2_r = int(o2[0],2)

    co2 = data.copy()

    i=0
    while len(co2)>1:
        su = 0
        for d in co2:
            if d[i] == "0":
                su-=1
            else:
                su+=1

        target=str(int(not su>=0))
        print(co2)
        print(f"{su} {target}")
        co2 = [co for co in co2 if co[i]==target]
        i+=1

    co2_r=int(co2[0],2)

    print(co2)

    return o2_r*co2_r

print(part2())