from datas import *

def score(problem,solution) :
    timeSaved = 0
    for request in problem.requests:
    #for each request, we calculat the time saved
        video = resquest.vid                                                                  # the video to stream
        endpoint = request.endpoint                                                           # the endpoint where to stream
        number = request.n                                                                    # number of time the video is streamed
        servers_with_video = filter(lambda s: v in s.videos, endpoints.servers.keys())        # keeping only the servers containg the video
        l = min(endpoint.latency,min(map(lambda s: endpoint.servers[s],servers_with_video)))  # best latency
        timeSaved += number * l                                                               # adding to the total time saved
    return (1000*timeSaved/(len(problem.requests)))                                           # returning average time saved
