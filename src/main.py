class Pizza():

    def __init__(self,t):
        self.pizza = t

class Problem():

    def __init__(self,p,r,c,l,h):
        self.pizza = p
        self.rows = r
        self.cols = c
        self.min_ingr = l
        self.max_cell = h

class Slice():

    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.width = w
        self.heigth = h
