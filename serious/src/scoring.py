from datas import *

def score(problem,solution) :
    timeSaved = 0
    for request in problem.requests:
    #for each request, we calculat the time saved
        video = resquest.vid                                           # the video to stream
        endpoint = request.endpoint                                    # the endpoint where to stream
        number = request.n                                             # number of time the video is streamed
        l = min(endpoint.latency,min(list(endpoint.servers.values()))) # best latency
        timeSaved += number * l
    return (1000*timeSaved/(len(problem.requests)))
