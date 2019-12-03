floors = [["PoG", "ThG", "ThC", "PrG", "RuG", "RuC", "CoG", "CoC"], ["PoC", "PrC"], [], [], [0]] #-1 is elevator, -1[0] is floor
test = [["HyC", "LiC"], ["HyG"], ["LiG"],[], [0]]


def is_valid(state):
    for floor in state[:-1]:
        gens =0
        for char in floor:
            if char[-1]=="G":
                gens += 1
            if char[-1]=="C" and char[:2]+"G" not in floor and gens > 0:
                return False
    return True
from itertools import combinations
from copy import deepcopy
#print(is_valid(test))
def get_moves(state):
    found = []
    floor = state[-1][0]
    can_move = list(combinations(state[floor], 2))+list(combinations(state[floor], 1))
    for move in can_move:

        new = deepcopy(state)
        new[-1].extend(move)
        for t in move:
            new[floor].remove(t)
        up, down = deepcopy(new), deepcopy(new)
        if floor < 3:
            up[-1][0] += 1
            up[up[-1][0]] = up[up[-1][0]]+up[-1][1:]
            up[-1] = [up[-1][0]]
            up = list(map(sorted, up))
            if is_valid(up):
                found.append(up)
        if floor >= 1:
            down[-1][0] -= 1
            down[down[-1][0]]=down[down[-1][0]]+down[-1][1:]
            down[-1] = [down[-1][0]]
            down = list(map(sorted, down))
            if is_valid(down):
                found.append(down)
    return found
def estimate(state):
    return state[-2]*4+state[-3]*3+state[-4]*2+state[-5]
import networkx as nx
def solve(state):
    seen = set()
    to_check = [(state, 0, 0)]
    found = False
    while to_check and not found:
        n,distance, est = to_check.pop(0)

        seen.add(tuple(map(tuple, n)))
        for possible in get_moves(n):
            if len(possible[-2])==4:
                print(distance+1)
                found = True
            if n!=possible and tuple(map(tuple, possible)) not in seen:
                to_check.append((possible, distance+1, estimate(possible)))
        if len(to_check)%1000==0:
            print(len(to_check), n, distance)
        to_check = sorted(to_check, key=lambda s: s[-1])


    """
    target = [[], [], [],["LiG", "HyG", "HyC", "LiC"], [0]]
    m = 9999
    for node in G.nodes:
        if len(node[-2])==10:
            a = nx.astar_path_length(G, tuple(map(tuple, state)), tuple(map(tuple, node)))
            if a < m:
                m = a
                print(m)"""
floors = list(map(sorted, floors))
test = list(map(sorted,test))
import time
start=  time.time()
solve(test)
print(time.time()-start)
