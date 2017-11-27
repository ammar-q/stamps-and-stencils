from collections import deque

class Component:
    def __init__(self, kpicture, startx, starty):
        self.elements = set()
        self.base = kpicture
        self.color = self.base[startx, starty]
        self.boundarycolors = set()
        
        queue = deque([(startx, starty)])
        visited = {}
        while len(queue):
            curx, cury = queue.popleft()
            visited[(curx, cury)] = True
            if 0 <= curx < self.base.dimx and 0 <= cury < self.base.dimy:
                if self.base[curx, cury] == self.color:
                    self.elements.add((curx, cury))
                    queue.extend([(curx + ii, cury + jj) for ii in range(-1,2) for jj in range(-1, 2) if not (curx + ii, cury + jj) in visited)
                else:
                    self.boundarycolors.add(self.base[curx, cury])
                    
        
    def add(self, e)
        self.elements.union(set(e))
    
    
    def boundary(self):
        border = set()
        for e in self.elements:
            for ii in range(-1, 2):
                for jj in range(-1, 2):
                    if (e[0] + ii, e[1] + jj) not in self.elements:
                        border.add(e)
    
        return border

    def __contains__(self, e):
        return e in self.elements
