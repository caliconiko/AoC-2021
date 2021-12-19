import numpy as np
from copy import deepcopy

with open("day18.txt") as f:
    raw = f.read()
    lines = [line.strip() for line in raw.strip().split("\n")]

def get_item(l, indices):
    current = l
    for i in indices:
        try:
            current = current[i]
        except TypeError:
            return None
    return current

def set_item(l, indices, val):
    current = l
    for i in indices[:len(indices)-1]:
        try:
            current = current[i]
        except TypeError:
            return None
    current[indices[-1]]=val
    return l

def part1():

    def explode(l):
        def check_down(l, indices=[]):
            if len(indices)==4 and type(get_item(l,indices)) is list:
                return indices

            for i in range(2):
                if get_item(l, indices+[i]):
                    c=check_down(l, indices+[i])
                    if c:
                        return c

        def check_down_direction(d, l, indices):
            if type(get_item(l,indices)) is not list:
                return indices

            return check_down_direction(d, l, indices+[d])

        indices = check_down(l)

        if indices is None:
            return None

        last0 = None
        for i in reversed(range(len(indices))):
            if indices[i] == 0:
                last0 = i
                break

        last1 = None
        for i in reversed(range(len(indices))):
            if indices[i] == 1:
                last1 = i
                break
        
        exploded = l.copy()

        if last1 is not None:
            left_indices = check_down_direction(1, l, indices[:last1]+[0])
            left=get_item(l, left_indices)

            exploded=set_item(exploded,left_indices,get_item(l, indices)[0]+left)

        if last0 is not None:
            right_indices = check_down_direction(0, l, indices[:last0]+[1])
            right=get_item(l, right_indices)

            exploded=set_item(exploded,right_indices,get_item(l, indices)[1]+right)

        exploded=set_item(exploded, indices, 0)

        return exploded

    def split_snail(l):
        def check_down(l, indices=[]):
            item = get_item(l,indices)
            if type(item) is not list and item>9:
                return indices

            for i in range(2):
                if get_item(l, indices+[i]):
                    c=check_down(l, indices+[i])
                    if c:
                        return c
        
        indices = check_down(l)
        if indices is None:
            return None

        will_split = get_item(l, indices)
        
        splitted = set_item(l, indices, [int(np.floor(will_split/2)), int(np.ceil(will_split/2))])

        return splitted

    def reduce(l):
        while True:
            exploded = explode(l)
            if exploded is not None:
                l=exploded
                continue

            splitted = split_snail(l)
            if splitted is not None:
                l=splitted
                continue

            return l

    def add_snail(a,b):
        return [a,b]

    def sum_snail(snails):
        s = snails[0]

        for sn in snails[1:]:
            s = add_snail(s,sn)
            s=reduce(s)

        return s

    def snail_magnitude(s, i=None):
        if type(s) is not list:
            if i==0:
                return s
            elif i==1:
                return s

        return 3*snail_magnitude(s[0], 0) + 2*snail_magnitude(s[1], 1)
    snails = [eval(l) for l in lines]
    print(snail_magnitude(sum_snail(snails)))
    
def part2():
    def explode(l):
        def check_down(l, indices=[]):
            if len(indices)==4 and type(get_item(l,indices)) is list:
                return indices

            for i in range(2):
                if get_item(l, indices+[i]):
                    c=check_down(l, indices+[i])
                    if c:
                        return c

        def check_down_direction(d, l, indices):
            if type(get_item(l,indices)) is not list:
                return indices

            return check_down_direction(d, l, indices+[d])

        indices = check_down(l)

        if indices is None:
            return None

        last0 = None
        for i in reversed(range(len(indices))):
            if indices[i] == 0:
                last0 = i
                break

        last1 = None
        for i in reversed(range(len(indices))):
            if indices[i] == 1:
                last1 = i
                break
        
        exploded = l.copy()

        if last1 is not None:
            left_indices = check_down_direction(1, l, indices[:last1]+[0])
            left=get_item(l, left_indices)

            exploded=set_item(exploded,left_indices,get_item(l, indices)[0]+left)

        if last0 is not None:
            right_indices = check_down_direction(0, l, indices[:last0]+[1])
            right=get_item(l, right_indices)

            exploded=set_item(exploded,right_indices,get_item(l, indices)[1]+right)

        exploded=set_item(exploded, indices, 0)

        return exploded

    def split_snail(l):
        def check_down(l, indices=[]):
            item = get_item(l,indices)
            if type(item) is not list and item>9:
                return indices

            for i in range(2):
                if get_item(l, indices+[i]):
                    c=check_down(l, indices+[i])
                    if c:
                        return c
        
        indices = check_down(l)
        if indices is None:
            return None

        will_split = get_item(l, indices)
        
        splitted = set_item(l, indices, [int(np.floor(will_split/2)), int(np.ceil(will_split/2))])

        return splitted

    def reduce(l):
        while True:
            exploded = explode(l)
            if exploded is not None:
                l=exploded
                continue

            splitted = split_snail(l)
            if splitted is not None:
                l=splitted
                continue

            return l

    def add_snail(a,b):
        return [a,b]

    def sum_snail(snails):
        s = snails[0]

        for sn in snails[1:]:
            s = add_snail(s,sn)
            s=reduce(s)

        return s

    def snail_magnitude(s, i=None):
        if type(s) is not list:
            if i==0:
                return s
            elif i==1:
                return s

        return 3*snail_magnitude(s[0], 0) + 2*snail_magnitude(s[1], 1)

    snails = [eval(l) for l in lines]

    mags=[]
    for i in range(len(snails)):
        for j in range(len(snails)):
            if i != j:
                ...
                sn = [snails[i].copy(), snails[j].copy()]
                sus = sum_snail(deepcopy(sn))
                mags.append(snail_magnitude(sus))
                
        # print(s1)
    mags.sort()
    # print(snails)

    print(mags[-1])

part2()