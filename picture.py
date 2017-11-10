import numpy as np
from PIL import Image
import easygui

class Picture:
    def __init__(self, path = ''):
        if not path:
            path = easygui.fileopenbox()
        self.im = Image.open(path).convert("RGBA")
        self.dimy, self.dimx = self.im.size
        self.im_data = np.array(self.im).reshape(self.dimx*self.dimy, -1)
        
    def show(self):
        self.im.show()
