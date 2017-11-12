import numpy as np
from PIL import Image
import easygui

class Picture:
    def __init__(self, path = ''):
        if not path:
            path = easygui.fileopenbox()
        self.im = np.array(Image.open(path).convert("RGBA"))
        self.dimx, self.dimy = self.im.shape[:2]
    
    def __getitem__(self, ii):
        return self.im[ii,:]
        
    def show(self):
        image = Image.fromarray(self.im.astype('uint8'), 'RGBA')
        image.show()
    
    def im_data(self):
        return np.array(self.im).reshape(self.dimx*self.dimy, -1)
