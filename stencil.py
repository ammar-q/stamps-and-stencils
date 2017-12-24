import numpy as np
from PIL import Image

class Stencil:
    def __init__(self, component, spray_color_idx):
        self.elements = component.elements
        self.boundary = component.boundary
        self.mask_color = component.color
        self.spray_color = component.base.colors[spray_color_idx]
        self.dimx = component.base.dimx
        self.dimy = component.base.dimy
        
    def save(self, path):
        canvas = np.zeros((self.dimx, self.dimy))
        for e in self.elements:
            canvas[e] = 1
        colors = np.vstack([self.spray_color, np.array([255,0,0])])
        Image.fromarray(colors[canvas.astype('uint8')].astype('uint8'), 'RGB').save(path)
    
    
    def apply(self, picture, color, startx = 0, starty = 0):
        if not color:
            color = self.spray_color
        for ii in range(self.dimx):
            for jj in range(self.dimy):
                if self.im[ii][jj] != self.mask_color:
                    picture.im[startx + ii][starty + jj] = color
