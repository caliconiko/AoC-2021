import numpy as np
from collections import defaultdict

with open("day21t.txt") as f:
    raw = f.read()
    lines = raw.splitlines()

def wrap_around(x, max):
    return x%max+(x%max==0)*max

def part1():
    player_positions = [int(l.split()[-1]) for l in lines]
    
    player_scores = np.array([0]*len(player_positions))

    i=0
    dice = 1
    while True:
        roll = wrap_around(dice,100)+wrap_around(dice+1, 100)+wrap_around(dice+2,100)

        player_index = i%2
        player_pos = player_positions[player_index]
        too_much = roll+player_pos
        new_player_pos = wrap_around(too_much, 10)

        player_scores[player_index]+=new_player_pos
        player_positions[player_index]=new_player_pos

        i+=1
        dice+=3
        if np.any(player_scores>=1000):
            print(player_scores[np.where(player_scores<1000)][0]*(dice-1))
            print()
            break

def part2():
    player_positions = [int(l.split()[-1]) for l in lines]
    
    player_scores = np.array([0]*len(player_positions))

    multiples = defaultdict(int)

    for i in range(3):
        for j in range(3):
            for k in range(3):
                multiples[i+j+k+3]+=1

    print(multiples)

    wins = [0,0]

    def split(roll, th, positions, scores, m):
        nonlocal multiples
        index = th%2
        new_pos = wrap_around(roll+positions[index], 10)

        scores[index]+= new_pos
        positions[index]=new_pos

        if np.any(scores>=21):
            wins[index]+=m
            print(wins)
            return

        for k in multiples.keys():
            split(k, th+1, positions.copy(), scores.copy(), multiples[k]*m)

    for k in multiples.keys():
        split(k, 0, player_positions.copy(), player_scores.copy(), multiples[k])
    print(wins)
part2()