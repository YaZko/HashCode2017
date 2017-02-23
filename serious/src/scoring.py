from datas import *

def score(problem,solution):
    timeSaved,total = 0,0
    for request in problem.requests:
    #for each request, we calculat the time saved
        video = request.vid                                                                   # the video to stream
        endpoint = request.endpoint                                                           # the endpoint where to stream
        number = request.n  
        servers_with_video = list(filter(lambda s: video.id in solution[s], endpoint.servers.keys()))  # keeping only the servers containg the video
        l = endpoint.latency
        if len(servers_with_video) != 0:
            l = min(l,min(list(map(lambda s: endpoint.servers[s],servers_with_video))))             # best latency
        timeSaved += number * (endpoint.latency-l)                                                               # adding to the total time saved
        total += number 
    return (1000*timeSaved/total)                                           # returning average time saved
