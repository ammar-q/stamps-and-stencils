class Stencil:
    def __init__(self, component, rgbcolor):
        self.mask_color = component.color
        self.spray_color = rgbcolor
        
        
    def show(self):
        
    
    
    def apply(self, picture, color, startx = 0, starty = 0):
        if not color:
            color = self.spray_color
        for ii in range(self.dimx):
            for jj in range(self.dimy):
                if self.im[ii][jj] != self.mask_color:
                    picture.im[startx + ii][starty + jj] = color
