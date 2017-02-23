from datas import *
from parser import *
from scoring import *
from solve import *

pb1 = parse("../inputs/example.in")
pb2 = parse("../inputs/kittens.in")
pb3 = parse("../inputs/me_at_the_zoo.in")
pb4 = parse("../inputs/trending_today.in")
pb5 = parse("../inputs/videos_worth_spreading.in")

sol1 = get_req(pb1)
print("Score of example : {}".format(score(pb1, sol1)))
sol2 = get_req(pb2)
print("Score of kittens : {}".format(score(pb2, sol2)))
sol3 = get_req(pb3)
print("Score of me at the zoo : {}".format(score(pb3, sol3)))
sol4 = get_req(pb4)
print("Score of trending today : {}".format(score(pb4, sol4)))
sol5 = get_req(pb5)
print("Score of videos worth spreading : {}".format(score(pb5, sol5)))

printer(sol1,"../inputs/example.out")
printer(sol2,"../inputs/kittens.out")
printer(sol3,"../inputs/me_at_the_zoo.out")
printer(sol4,"../inputs/trending_today.out")
printer(sol5,"../inputs/videos_worth_spreading.out")

