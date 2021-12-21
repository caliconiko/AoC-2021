import numpy as np


with open("day15t.txt") as f:
    raw = f.read()
    lines = [line.strip() for line in raw.strip().split("\n")]

def part1():
    risk_map = np.array([[int(n) for n in l] for l in lines])

    all_the_paths = []

    def get_path(risks, current_index):
        nonlocal risk_map
        if current_index == (risk_map.shape[0]-1, risk_map.shape[1]-1):
            all_the_paths.append(risks+risk_map[current_index])
            # print("ASDASD")
            return

        if current_index[0]< risk_map.shape[0]-1:
            next_index = (current_index[0]+1, current_index[1])
            get_path(risks+risk_map[current_index], next_index)

        if current_index[1]< risk_map.shape[1]-1:
            next_index = (current_index[0], current_index[1]+1)
            get_path(risks+risk_map[current_index], next_index)
    
    get_path([], (0,0))

    print(all_the_paths)
        

    print(np.array(risk_map).shape)


part1()