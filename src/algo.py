from data import *

#Should return list of slices
def decoupage(problem):
    min_ingr = problem.min_ingr
    max_ingr = problem.max_cell
    cols = problem.pizza.cols
    rows = problem.pizza.rows
    slices = []
    y1 = 0
    y2 = rows - 1
    for col in range(cols-1):
        x1 = col
        x2 = col + 1
        sli = Slice(x1, y1, x2, y2)

        #as long as we don't have a valid slide make it bigger
        while (not problem.valid(sli)):
            #if we reach the end of the pizza and the slice is not valid
            if (x2 >= cols):
                return slices
            x2 += 1
            sli = Slice(x1, y1, x2, y2)


        #When we have a valid slice we try to make it max size
        while (problem.valid(sli)):
            if (x2 >= cols):
                break
            sli = Slice(x1, y1, x2, y2)
            x2 += 1
        col = x2
        slices.append(sli)

