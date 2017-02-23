import os
from datas import *

def parse(path):
    content = open(path)
    params = split_int(content)
    nb_vids = params[0]
    nb_ends = params[1]
    nb_reqs = params[2]
    nb_caches = params[3]
    capa = params[4]

    vids_sz = split_int(content)
    vids = []
    for i in range(nb_vids):
        vids.append(Video(vids_sz[i], i))

    ends = []
    for i in range(nb_ends):
        end_params = split_int(content)
        latency_end_data = end_params[0]
        nb_caches_to_e = end_params[1]
        connections = {}
        for j in range(nb_caches_to_e):
            connection_param = split_int(content)
            id_cache = connection_param[0]
            lat_end_cache = connection_param[1]
            connections[id_cache] = lat_end_cache
        end = EndPoint(latency_end_data, i, connections)
        ends.append(end)

    reqs = []
    for i in range(nb_reqs):
        req = split_int(content) 
        reqs.append(Request(req[0], ends[req[1]], req[2]))

    servs = [ Server(i) for i in range(nb_caches)]
    assert(nb_caches == len(servs))
    assert(nb_ends == len(ends))
    assert(nb_vids == len(vids))
    assert(nb_reqs == len(reqs))

    return Problem(capa, nb_caches, servs, \
            nb_ends, ends, \
            nb_vids, vids,
            nb_reqs, reqs)

    # print(params)
    # print(vids_sz)
    # print(ends)


def split_int(content):
    params = content.readline().split()
    return [ int(i) for i in params ]


def printer(dic_servers, output_file):
    ofile = open(output_file, "w")
    ofile.write(str(len(dic_servers.keys())))
    ofile.write("\n")
    for k, v in dic_servers.items():
        output = list(k) + v
        output = " ".join([str(i) for i in output])
        ofile.write(output)
        ofile.write("\n")
    ofile.close()

if __name__ == "__main__":
    print(parse("../inputs/me_at_the_zoo.in"))

