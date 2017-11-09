from PIL import Image
import easygui

class Picture:
    def __init__(self, path = ''):
        if not path:
            path = easygui.fileopenbox()
        self.im = Image.open(path).convert("RGBA")
        self.dim_x, self.dim_y = self.im.size
        self.im_data = np.array(self.im).reshape(-1, 4)
        
