from data import *


def solve1(pb):
    sol = []
    p = pb.pizza
    size = min(pb.max_cell-1,p.cols-1)
    for idx,r in enumerate(p.pizza):
        s = Slice(idx,0,idx,size)
        if pb.valid(s):
            sol.append(s)
    return sol

def solve(pb):
    sol = []
    p = pb.pizza
    size = min(pb.max_cell-1,p.cols-1)
    for idx,r in enumerate(p.pizza):
        s = Slice(idx,0,idx,size)
        i = 0
        while (not pb.valid(s) and i + size + 1 < p.cols):
            i += 1
            s = Slice(idx,i , idx, i+size)
        if pb.valid(s):
            sol.append(s)
    return sol
