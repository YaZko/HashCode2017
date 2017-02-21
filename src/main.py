from data import *
from parser import *
from solver import *
import os

pb = parse("../inputs/small.in")
p = pb.pizza
# print(decoupage(pb))
# for s in decoupage(pb):
    # print(s)

os.makedirs("output", exist_ok=True)
pb1 = parse("../inputs/small.in")
pb2 = parse("../inputs/example.in")
pb3 = parse("../inputs/medium.in")
pb4 = parse("../inputs/big.in")
print(pb)
s = Slice(0,0,0,4)
#print(solve(pb))
printer(solve(pb1), "output/out_small")
printer(solve(pb2), "output/out_example")
printer(solve(pb3), "output/out_medium")
printer(solve(pb4), "output/out_big")


# p = parse("../inputs/small.in")
# p = parse("../inputs/small.in")
# p = parse("../inputs/small.in")

