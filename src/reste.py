from data import *
from parser import *
from solver import *

#Renvoie une liste de morceaux de pizzas
def recupere_reste(problem, lslices):
    problem.pizza = enlever_slice(problem, lslices)
    print(pb)
    repere_pizz(problem)
    print(pb)
    return problem
    
def repere_pizz(problem):
    row = 0
    col = 0
    slices = []
    for row in range(problem.pizza.rows):
        for col in range(problem.pizza.cols):
            if not problem.pizza.pizza[row][col] is None:
                sli = get_rest(problem, row, col, False)
                if problem.valid(sli):
                    slices.append(sli)
                    problem.pizza = enlever_slice(problem, [sli])
    return slices


def get_rest(problem, row, col, ligne):
    pizza = problem.pizza
    row2 = row
    col2 = col
    if ligne:
        while (col2 + 1 < pizza.cols) \
        and (not pizza.pizza[row2][col2 + 1] is None) \
        and (col2 - col < problem.max_cell):
            col2 += 1
    else:
        while (row2 + 1 < pizza.rows) \
        and (not pizza.pizza[row2+1][col2] is None) \
        and (row2 - row < problem.max_cell):
            row2 += 1
    return Slice(row,col,row2,col2)


#enleve les slices de la pizza
def enlever_slice(problem, lslices):
    pizza = problem.pizza
    for s in lslices:
        surf = surface(s)
        for row in surf[0]:
            for col in surf[1]:
                pizza.pizza[row][col] = None
    return pizza


def surface(sli):
    if sli.x1 > sli.x2:
        r2 = sli.x1
        r1 = sli.x2
    else:
        r2 = sli.x2
        r1 = sli.x1
    if sli.y1 > sli.y2:
        c2 = sli.y1
        c1 = sli.y2
    else:
        c2 = sli.y2
        c1 = sli.y1
    res = range(r1, r2+1), range(c1, c2+1)
    return res


if __name__ == "__main__":
    pb = parse("../inputs/small.in")
    p = pb.pizza
    print(pb)
    slices = [Slice(0,0,0,4), \
            Slice(1,0,1,4), \
            Slice(2,0,2,4), \
            Slice(3,0,3,4), \
            Slice(4,2,4,6), \
            Slice(5,2,5,6)]
    pb = recupere_reste(pb, slices)
