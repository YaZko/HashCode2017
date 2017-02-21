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

def scoring(sol):
    return sum([s.size() for s in sol])

def solve(pb, w, h):
    sol = []
    p = pb.pizza
    w = min(p.cols,w)
    h = min(p.rows,h)
    r,c = 0,0
    while r+h <= p.rows:
        # print("currently, r = {} and c = {}".format(r,c))
        b = False
        while c+w <= p.cols:
            # print("Inner, r = {} and c = {}".format(r,c))
            s = Slice(r,c,r+h-1,c+w-1)
            if pb.valid(s):
                b = True
                sol.append(s)
                c += w 
            else:
                c += 1
        if b:
            r += h
        else:
            r += 1
        c = 0
    return sol

def super_solve(pb):
    best,sol = 0,[]
    for w in range(1,pb.max_cell+1):
        h = pb.max_cell//w
        # print("Solving with w = {} and h = {}\n".format(w,h))
        s = solve(pb,w,h)
        # print(scoring(s))
        if scoring(s) > best:
            best = scoring(s)
            sol = s
    return sol
