from picture import *
from kpicture import *
from stamp import *
from stencil import *
from componentresolver import *

import numpy as np



# Set main picture
k = 2
base = Picture()
kbase = kPicture(base, k)



####################
#### Stamp flow ####
####################

front_design = kbase
back_design = kPicture(Picture(), 2)
mask = kPicture(Picture(), 2)

back_color = index_opaque(back_design.colors)
mask_color = index_opaque(mask.colors)

stamps = []
for front_color in range(k):
    print('Building stamp {}'.format(front_color))
    stamps.append(Stamp(front_design, back_design, mask, front_color, back_color, mask_color, front_raise = 100, back_raise = 30, center = 60))
    stamps[-1].save('stamp{}.stl'.format(front_color))
