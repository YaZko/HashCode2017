from data import *
from parser import *
from algo import *

pb = parse("../inputs/small.in")
p = pb.pizza
for s in decoupage(pb):
    print(s)

