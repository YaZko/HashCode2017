class Pizza():

    def __init__(self,t,r,c):
        self.pizza = t
        self.rows = r
        self.cols = c

    def __str__(self):
        s = "-"*(2 * self.cols + 1) + "\n"
        for r in self.pizza:
            for i in r:
                s = s + ("T " if i else "M ")
            s = s + "\n"
        return s

    def __repr__(self):
        s = "-"*(2 * self.cols + 1) + "\n"
        for r in self.pizza:
            for i in r:
                s = s + ("T " if i else "M ")
            s = s + "\n"
        return s

class Problem():

    def __init__(self,p,r,c,l,h):
        self.pizza = Pizza(p,r,c)
        self.min_ingr = l
        self.max_cell = h

    def __str__(self):
        s = "We seek slices with\n* at least {} of each ingredient\n* at most {} ingredients\n".format(self.min_ingr,self.max_cell)
        s = s + "The pizza is the following one:\n"
        s = s + str(self.pizza)
        return s

    # Tests whether a slice is valid.
    # Be careful, we will still need to enforce that none of them overlap
    def valid(self,s):
        ts = len([i for i in r for r in self.pizza if i])
        tot = s.size()
        not_too_much = tot <= self.max_cell
        enough_T = ts >= self.min_ingr
        enough_M = tot-ts >= self.min_ingr
        return not_too_much and enough_T and enough_M

class Slice():

    def __init__(self,x1,y1,x2,y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.width = x2 - x1
        self.height = y2 - y1
        self.nb_tot = self.width * self.height

    def size(self):
        return self.width * self.height

    def __repr__(self):
        return "top-left: (" + self.x1 + ", " + \
                self.y1 + ") --- bottom-right: ("  +  \
                self.x2 + ", " + self.y2
