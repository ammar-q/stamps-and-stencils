def add_border(kpicture, thickness, color = -1):
    tmp = np.full((kpicture.dimx, thickness), -1)
    kpicture.im = np.hstack((tmp, kpicture.im, tmp))
    tmp = np.full((thickness, kpicture.dimy + 2*thickness), -1)
    kpicture.im = np.vstack((tmp, kpicture.im, tmp))
    
    
class Stencil:
    def __init__():
    
    def show():
    
    def apply():
    
