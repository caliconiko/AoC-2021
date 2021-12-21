from typing import List
from numpy import Infinity 

with open("day15t.txt") as f:
    raw = f.read()
    lines = raw.splitlines()

class Node:
    def __init__(self, risk, x, y) -> None:
        self.risk = risk
        self.x = x
        self.y = y

        self.connections:List[Node] = []

        self.via = None
        self.distance = Infinity
        self.cost = Infinity

    def __repr__(self) -> str:
        return f"R{self.risk}"


def part1():
    risks = [[int(n) for n in l] for l in lines]
    print(risks)

    nodes:List[List[Node]]=[]
    for i, l in enumerate(risks):
        ln = []
        for j, r in enumerate(l):
            ln.append(Node(r, i, j))
        nodes.append(ln)


    for i, l in enumerate(nodes):
        for j, n in  enumerate(l):
            for d in [-1, 1]:
                if d+i>=0 and d+i<len(nodes):
                    n.connections.append(nodes[d+i][j])
                if d+j>=0 and d+j<len(nodes):
                    n.connections.append(nodes[i][d+j])

    goal = nodes[-1][-1]

    
part1()