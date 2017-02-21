class Pizza():

    def __init__(self,t,r,c):
        self.pizza = t
        self.rows = r
        self.cols = c
 
class Problem():

    def __init__(self,p,r,c,l,h):
        self.pizza = Pizza(p,r,c)
        self.min_ingr = l
        self.max_cell = h

    def valid(self,s):
        ts = size([i for i in r for r in self.pizza if i])
        return s.size() <= self.max_cell 

class Slice():

    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.width = w
        self.height = h

    def size(self):
        return self.width * self.height


