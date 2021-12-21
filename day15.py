from __future__ import annotations
from typing import List
from numpy import Infinity, sqrt 
from functools import total_ordering
import numpy as np

with open("day15.txt") as f:
    raw = f.read()
    lines = raw.splitlines()

@total_ordering
class Node:
    def __init__(self, risk, x, y) -> None:
        self.risk = risk
        self.x = x
        self.y = y

        self.connections:List[Node] = []

        self.via = None
        self.distance = Infinity
        self.heuristic = Infinity
        self.explored = False

    def __repr__(self) -> str:
        return f"R{self.risk}"

    def __lt__(self, other):
        return self.heuristic < other

    def __eq__(self, other):
        return self.heuristic == other

    def __add__(self, other):
        return self.risk+other

    def __radd__(self, other):
        return self.__add__(other)

    def physical_distance_to(self, node:Node):
        return sqrt((node.x-self.x)**2 + (node.y-self.y)**2)

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
    start = nodes[0][0]

    start.distance = 0
    start.heuristic = start.physical_distance_to(goal)

    queue = [start]

    while len(queue)>0:
        current = queue.pop(0)

        to_explore = current.connections
        
        for being_explored in to_explore:
            potential_new_distance = current.distance+being_explored.risk

            if potential_new_distance<being_explored.distance:
                being_explored.via = current
                being_explored.distance = potential_new_distance
                being_explored.heuristic = being_explored.distance+being_explored.physical_distance_to(goal)

                queue.append(being_explored)

        queue.sort()

    # get path 
    path = []

    current_via = goal
    while current_via.via is not None:
        path.append(current_via)
        current_via = current_via.via
    

    print(sum(path))

def part2():
    def wrap_around(x):
        return x%9+((x%9)==0)*9
    
    # risks = [[int(n) for n in l] for l in lines]
    partial_risks = np.array([[int(n) for n in l] for l in lines])
    risks_column = partial_risks.copy()

    for i in range(4):
        to_be_stacked = partial_risks+i+1
        to_be_stacked = wrap_around(to_be_stacked)

        risks_column = np.hstack((risks_column, to_be_stacked))
    
    risks = risks_column.copy()

    for i in range(4):
        to_be_stacked = risks_column+i+1
        to_be_stacked = wrap_around(to_be_stacked)

        risks = np.vstack((risks, to_be_stacked))

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
    start = nodes[0][0]

    start.distance = 0
    start.heuristic = start.physical_distance_to(goal)

    queue = [start]

    while len(queue)>0:
        current = queue.pop(0)
        current.explored = True
        to_explore = current.connections
        
        for being_explored in to_explore:
            potential_new_distance = current.distance+being_explored.risk

            if potential_new_distance<being_explored.distance:
                being_explored.via = current
                being_explored.distance = potential_new_distance
                being_explored.heuristic = being_explored.distance+being_explored.physical_distance_to(goal)

                if not being_explored.explored:
                    queue.append(being_explored)
                        

        queue.sort()
        print(len(queue))

    # get path 
    path = []

    current_via = goal
    while current_via.via is not None:
        path.append(current_via)
        current_via = current_via.via
    

    print(sum(path))
    
part2()