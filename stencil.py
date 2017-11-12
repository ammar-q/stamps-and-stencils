def add_border(kpicture, thickness, color = -1):
    tmp = np.full((kpicture.dimx, thickness), -1)
    kpicture.im = np.hstack((tmp, kpicture.im, tmp))
    tmp = np.full((thickness, kpicture.dimy + 2*thickness), -1)
    kpicture.im = np.vstack((tmp, kpicture.im, tmp))
    
    
class Stencil:
    def __init__():
    
    def show(self):
        
    
    
    def apply(self, picture, color, startx = 0, starty = 0):
        for ii in range(self.dimx):
            for jj in range(self.dimy):
                if self.im[ii][jj] != self.mask_color:
                    picture.im[startx + ii][starty + jj] = color
