import numpy as np
import queue

with open("day6.txt") as f:
    raw = f.read()
    lines = [line.strip() for line in raw.strip().split("\n")]

def part1():
    times=np.array([int(n) for n in lines[0].split(",")])
    for _ in range(80):
        times-=1
        reset = np.where(times<0)
        times[reset]=6
        times = np.append(times, np.full(len(reset[0]), 8))
        print(times)
    print(times)
    print(len(times))
    ...

def part2a():
    times=np.array([int(n) for n in lines[0].split(",")])
    for _ in range(256):
        times-=1
        reset = np.where(times<0)
        times[reset]=6
        times = np.append(times, np.full(len(reset[0]), 8))
        print(f"{times} {_}")
    print(times)
    print(len(times))
    ...

def part2q():
    init=[int(n) for n in lines[0].split(",")]
    time_queue = queue.SimpleQueue()
    q_size = 0

    for n in init:
        time_queue.put(n)
        q_size+=1
    
    for _ in range(256):
        for __ in range(q_size):
            t = time_queue.get()
            if t==0:
                time_queue.put(6)
                time_queue.put(8)
                q_size+=1
            else:
                time_queue.put(t-1)
        print(f"{q_size} {_}")

    print(q_size)
    print()

def part2s():
    times="".join([n for n in lines[0].split(",")])
    
    for _ in range(256):
        # print(times)
        times=times.replace("0", "-")
        for i in range(1, 9):
            times=times.replace(str(i), str(i-1))
        times=times.replace("-", "68")
        print(_)
        

    print(len(times))

def part2():
    times=[0]*9

    for n in lines[0].split(","):
        times[int(n)]+=1

    for _ in range(256):

        moar = times[0]
        for i in range(1,9):
            times[i-1]=times[i]
            times[i]=0
        times[6]+=moar
        times[8]+=moar
    
    print(np.sum(times))

part2()