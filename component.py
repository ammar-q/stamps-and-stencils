from collections import deque



class Component:
    def __init__(self, kpicture, startx, starty):
        self.elements = set()
        self.base = kpicture
        self.color = self.base[startx][starty]
        self.boundary = set()
        
        queue = deque([(startx, starty)])
        visited = {}
        while len(queue):
            curx, cury = queue.popleft()
            print("{}, {}".format(curx, cury))
            if 0 <= curx < self.base.dimx and 0 <= cury < self.base.dimy and not (curx, cury) in visited:
                visited[(curx, cury)] = True
                if self.base[curx][cury] == self.color:
                    self.elements.add((curx, cury))
                    queue.extend([(curx + ii, cury + jj) for ii in range(-1,2) for jj in range(-1, 2) if not (curx + ii, cury + jj) in visited])
                else:
                    self.boundary.add((curx, cury))

    def adj(self, other):
        return any(e in other.elements for e in self.boundary)
        
    def merge(self, other):
        self.elements = self.elements.union(other.elements)
        self.boundary = self.boundary.union(other.boundary).difference(self.elements)
        
