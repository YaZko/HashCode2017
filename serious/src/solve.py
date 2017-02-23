from datas import *
from parser import *
from scoring import *

def get_req(pb):

    # We initialize a dictionnary mapping servers to dictionnaries mapping vids to number of accessible requests
    d = {s:{v:0 for v in range(pb.nb_vids)} for s in range(pb.nb_servers)}
    for r in pb.requests:
        e = r.endpoint
        v = r.vid
        n = r.n
        for s in e.servers:
            d[s][v.id] = d[s][v.id] + r.n

    # for a,b in d.items():
    #     print("{}: {}".format(a,b))

    sol = [[] for s in range(pb.nb_servers)]

    for s in range(pb.nb_servers):
        # We sort the videos for each server by ratio (number of requests)/(size of videos)
        l = sorted(d[s].items(),key=lambda x: x[1]/pb.vids[x[0]].size,reverse=True)
        for v,n in l:
            # print(pb.servers[s].load + pb.vids[v].size)
            if pb.servers[s].load + pb.vids[v].size <= pb.capacity:
                sol[s].append(v)
                pb.servers[s].load += pb.vids[v].size

    return sol

# pb = parse("../inputs/example.in")
# sol = get_req(pb)
