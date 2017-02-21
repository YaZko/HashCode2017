from data import *
import os

def parse(path):
    content = open(path).readlines()
    params = content[0].split()
    pizza = content[1:]
    pizza = [ i.strip() for i in pizza]
    for i in range(len(pizza)):
        pizza[i] = [ tomata_mush(c) for c in pizza[i]]
    pizza = pizza
    return Problem(pizza, int(params[0]), int(params[1]), int(params[2]), int(params[3]))

def tomata_mush(c):
    if c == 'T':
        return True
    else:
        return False

def printer(lslices):
    print(lslices)
    ofile = open("output", "w")
    ofile.write(str(len(lslices)))
    ofile.write("\n")
    for s in lslices:
        output = [ s.x1, s.y1, s.x2, s.y2 ]
        output = " ".join([str(i) for i in output])
        print(output)
        ofile.write(output)
        ofile.write("\n")
    ofile.close()


if __name__ == "__main__":
    print(parse("../inputs/small.in"))

