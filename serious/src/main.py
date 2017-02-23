from datas import *
from parser import *
from scoring import *
from solve import *

pb1 = parse("../inputs/example.in")
pb2 = parse("../inputs/kittens.in")
pb3 = parse("../inputs/me_at_the_zoo.in")
pb4 = parse("../inputs/trending_today.in")
pb5 = parse("../inputs/videos_worth_spreading.in")


printer(get_req(pb1),"../inputs/example.out")
printer(get_req(pb2),"../inputs/kittens.out")
printer(get_req(pb3),"../inputs/me_at_the_zoo.out")
printer(get_req(pb4),"../inputs/trending_today.out")
printer(get_req(pb5),"../inputs/videos_worth_spreading.out")
