from data import *

def same_slice(r1,c1,r2,c2,slices):
    return 1

def print_sliced_pizza(pizza, slices):
    visu = "-"*(1+2*pizza.cols) 
    visu = visu + "\n"
    for id_l,l in enumerate(pizza.pizza[:-1]):
        #print a line of the pizza
        visu = visu + "|"
        for id_c,b in enumerate(l[:-1]):
            if b:
                visu = visu + "T"
            else:
                visu = visu + "M"
            if same_slice(id_l,id_c,id_l,id_c+1,slices):
                visu = visu + " "
            else:
                visu = visu + "|"
        if l[-1]:
            visu = visu + "T"
        else:
            visu = visu + "M"
        visu = visu + "|\n"
        #print a line of space
        visu = visu + "|"
        for id_c,b in enumerate(l):
            if same_slice(id_l,id_c,id_l+1, id_c,slices):
                visu = visu + " "
            else:
                visu = visu + "-"
            visu = visu + "+"
        visu = visu + "\n"
    #print last real line
    visu = visu + "|"
    for id_c,b in enumerate(pizza.pizza[-1][:-1]):
        if b:
            visu = visu + "T"
        else:
            visu = visu + "M"
        if same_slice(pizza.rows,id_c,pizza.rows,id_c+1,slices):
            visu = visu + " "
        else:
            visu = visu + "|"
    if pizza.pizza[-1][-1]:
        visu = visu + "T"
    else:
        visu = visu + "M"
    visu = visu + "|\n"
    visu = visu + "-"*(1+2*pizza.cols)
        

    return visu

