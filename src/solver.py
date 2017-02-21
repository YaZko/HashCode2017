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

def solve2(pb):
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

def solve3(pb):
    sol = []
    p = pb.pizza
    size = min(pb.max_cell-1,p.cols-1)
    for idx,r in enumerate(p.pizza):
        i = 0
        while (i + size < p.cols):
            s = Slice(idx,i,idx,i+size)
            if pb.valid(s):
                sol.append(s)
                i = i + size + 1
            else:
                i += 1
    return sol

# def solve(pb, w, h):
#     sol = []
#     p = pb.pizza
#     r,c = 0,0
#     while r+w < p.cols:
#         while c+h < p.rows:
#             s = Slice(r,c,r+w,c+h)
#             if pb.valid(s):
#                 sol.append(s)
#                 c += w + 1
