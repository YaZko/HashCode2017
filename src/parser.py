
from main import *

def parse(path):
    content = open(path).readlines()
    params = content[0].split()
    pizza = content[1:]
    pizza = [ i.strip() for i in pizza]
    for i in range(len(pizza)):
        pizza[i] = [ tomata_mush(c) for c in pizza[i]]
    pizza = Pizza(pizza)
    return Problem(pizza, params[0], params[1], params[2], params[3])

def tomata_mush(c):
    if c == 'T':
        return True
    else:
        return False

if __name__ == "__main__":
    print(parse("../inputs/small.in"))


