from data import *
from parser import *
from solver import *
from visualisator import *
import os

pb = parse("../inputs/small.in")
p = pb.pizza

# w = 2
# h = pb.max_cell // 2
# s = solve(pb,w,h)

s = super_solve(pb)
print(print_sliced_pizza(p, s))



# os.makedirs("output", exist_ok=True)
# pb1 = parse("../inputs/small.in")
# pb2 = parse("../inputs/example.in")
# pb3 = parse("../inputs/medium.in")
# pb4 = parse("../inputs/big.in")
# # print(pb)
# # s = Slice(0,0,0,4)
# #print(solve(pb))
# printer(super_solve(pb1), "output/out_small")
# printer(super_solve(pb2), "output/out_example")
# printer(super_solve(pb3), "output/out_medium")
# printer(super_solve(pb4), "output/out_big")


# p = parse("../inputs/small.in")
# p = parse("../inputs/small.in")
# p = parse("../inputs/small.in")

