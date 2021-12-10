import numpy as np
import re

with open("day10.txt") as f:
    raw = f.read()
    lines = [line.strip() for line in raw.strip().split("\n")]

def part1():
    kind = re.compile('[\[{(<][\]})>]')
    not_kind = re.compile('(\[\]|\{\}|\(\)|<>)')

    table = {
        ')':3,
        ']':57.,
        '}':1197,
        '>':25137,
    }
    points = 0
    ...
    for l in lines:
        lm=l
        print(l)
        while kind.search(lm) is not None:
            m = kind.search(lm)
            start, end = m.span()
            grr = m.group()

            kindnt = not_kind.match(grr)

            if kindnt is None:
                points+=table[grr[-1]]
                break

            lmnext = lm[:start]+lm[end:]
            lm=lmnext

            print(f"{lm} {start=} {end=}")
        print("----------")
    print(points)


def part2bad():
    kind = re.compile('[\[{(<][\]})>]')
    not_kind = re.compile('(\[\]|\{\}|\(\)|<>)')

    ...
    cor = []
    for i, l in enumerate(lines):
        lm=l

        while kind.search(lm) is not None:
            m = kind.search(lm)
            start, end = m.span()
            grr = m.group()

            kindnt = not_kind.match(grr)

            if kindnt is None:
                cor.append(i)
                break

            lmnext = lm[:start]+lm[end:]
            lm=lmnext

    incom = lines.copy()
    for i in cor:
        incom[i]=0
    while 0 in incom:
        incom.remove(0)
    print(incom)
    table = {
        ')':1,
        ']':2,
        '}':3,
        '>':4,
    }
    points = 0

    pair = {
        '(':')',
        '[':']',
        '{':'}',
        '<':'>',
        ')':'(',
        ']':'[',
        '}':'{',
        '>':'<'
    }

    topen = {
        '(':'(',
        '[':'[',
        '{':'{',
        '<':'<',
        ')':'(',
        ']':'[',
        '}':'{',
        '>':'<'
    }

    opening = '([{<'
    closing= ')]}>'

    for inc in incom:
        so_far = {
            '(':0,
            '[':0,
            '{':0,
            '<':0,
            }

        for c in inc:
            if c in opening:
                so_far[topen[c]]+=1
            else:
                so_far[topen[c]]-=1
        print(f"{inc} {so_far}")
    
    ...

def part2():
    kind = re.compile('[\[{(<][\]})>]')
    not_kind = re.compile('(\[\]|\{\}|\(\)|<>)')

    ...
    cor = []
    for i, l in enumerate(lines):
        lm=l

        while kind.search(lm) is not None:
            m = kind.search(lm)
            start, end = m.span()
            grr = m.group()

            kindnt = not_kind.match(grr)

            if kindnt is None:
                cor.append(i)
                break

            lmnext = lm[:start]+lm[end:]
            lm=lmnext

    incom = lines.copy()
    for i in cor:
        incom[i]=0
    while 0 in incom:
        incom.remove(0)
    print(incom)

    the_things = []

    for inc in incom:
        lm=inc

        while not_kind.search(lm) is not None:
            m = kind.search(lm)
            start, end = m.span()
            grr = m.group()

            lmnext = lm[:start]+lm[end:]
            lm=lmnext

        the_things.append(lm)


    table = {
        '(':1,
        '[':2,
        '{':3,
        '<':4,
    }
    points = []

    for the_thing in the_things:
        cur_p = 0
        for t in the_thing[::-1]:
            cur_p*=5
            cur_p+=table[t]
        points.append(cur_p)

    points.sort()

    print(points[len(points)//2])

    print(points)
    
    ...

part2()