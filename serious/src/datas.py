class Problem():

    def __init__(self,c,ns,s,ne,e,nv,v,nr,r):

        self.capacity = c     # Capacity of each server
        self.nb_servers = ns  # Number of cache servers
        self.servers = s      # Mapping from server's id to servers

        self.nb_endpoints = ne  # Number of endpoints
        self.endpoints = e      # List of endpoints

        self.nb_vids = nv     # Number of videos
        self.vids = v         # List of videos

        self.nb_requests = nr # Number of requests
        self.requests = r     # List of requests

class Request():

    def __init__(self,v,e,n):
        self.vid = v         # Video requested
        self.endpoint = e    # endpoint requesting
        self.n = n           # Number of requests

class Video():

    def __init__(self,s,id):
        self.size = s     # Size of the video
        self.id = id      # Video's id
        self.servers = [] # List of servers in which one the video is cached

class Server():

    def __init__(self,id):
        self.id = id
        self.videos = []
        self.load = 0

class EndPoint():

    def __init__(self,t,id,d):

        self.latency = t  # Latency to the data center
        self.id      = id
        self.servers = d  # A dictionnary mapping connected servers to their latency


# A solution is a dictionnary mapping servers' id to list of videos.
