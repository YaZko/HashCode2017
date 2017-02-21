from data import *
from parser import *
from solver import *

pb = parse("../inputs/small.in")
p = pb.pizza
# print(decoupage(pb))
# for s in decoupage(pb):
    # print(s)


pb = parse("../inputs/small.in")
print(pb)
s = Slice(0,0,0,4)
#print(solve(pb))
printer(solve(pb))

# p = parse("../inputs/small.in")
# p = parse("../inputs/small.in")
# p = parse("../inputs/small.in")

