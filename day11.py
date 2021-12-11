import numpy as np

with open("day11.txt") as f:
    raw = f.read()
    lines = [line.strip() for line in raw.strip().split("\n")]

def part1():
    ...
    octs = np.array([[int(n) for n in l] for l in lines])

    print(octs)

    adjacents = ((0,1),(1,0),(1,1),(-1,1),(0,-1),(-1,0),(-1,-1),(1,-1))

    flashes_that_happened = 0

    for i in range(200):
        octs+=1
        flashed = (octs>9).astype(np.int32)
        where_flashed = np.where(flashed==1)
        for y,x in zip(*where_flashed):
            flashes_that_happened+=1

            for adj in adjacents:
                to_add = np.array((y,x))+np.array(adj)

                if not( np.any(to_add>9) or np.any(to_add<0)):
                    ...
                    octs[to_add[0]][to_add[1]]+=1
                # print(to_add)

        while not np.all((flashed>0)==(octs>9)):
            flashed = flashed+(octs>9).astype(np.int32)
            where_flashed = np.where(flashed==1)
            for y,x in zip(*where_flashed):
                flashes_that_happened+=1
                
                for adj in adjacents:
                    to_add = np.array((y,x))+np.array(adj)

                    if not( np.any(to_add>9) or np.any(to_add<0)):
                        ...
                        octs[to_add[0]][to_add[1]]+=1
                    # print(to_add)
                

        octs[np.where(octs>9)]=0
        print(flashes_that_happened)

def part2():
    ...
    octs = np.array([[int(n) for n in l] for l in lines])

    print(octs)

    adjacents = ((0,1),(1,0),(1,1),(-1,1),(0,-1),(-1,0),(-1,-1),(1,-1))

    flashes_that_happened = 0
    i=0
    while True:
        octs+=1
        flashed = (octs>9).astype(np.int32)
        where_flashed = np.where(flashed==1)
        for y,x in zip(*where_flashed):
            flashes_that_happened+=1

            for adj in adjacents:
                to_add = np.array((y,x))+np.array(adj)

                if not( np.any(to_add>9) or np.any(to_add<0)):
                    ...
                    octs[to_add[0]][to_add[1]]+=1
                # print(to_add)

        while not np.all((flashed>0)==(octs>9)):
            flashed = flashed+(octs>9).astype(np.int32)
            where_flashed = np.where(flashed==1)
            for y,x in zip(*where_flashed):
                flashes_that_happened+=1
                
                for adj in adjacents:
                    to_add = np.array((y,x))+np.array(adj)

                    if not( np.any(to_add>9) or np.any(to_add<0)):
                        ...
                        octs[to_add[0]][to_add[1]]+=1
                    # print(to_add)
                

        octs[np.where(octs>9)]=0
        if np.all(octs==0):
            print("WHOA")
            print(i+1)
            break
        i+=1

part2()