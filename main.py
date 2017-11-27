from picture import *
from kpicture import *
from stamp import *
#from stencil import *
from componentresolver import *

import numpy as np



# Set main picture
k = 1
base = Picture()
kbase = kPicture(base, k)


####################
#### Stamp flow ####
####################

front_design = kbase

try:
    back_design = Picture()
except:
    back_design = None

try:
    mask = Picture()
except:
    mask = None

stamps = []
for front_color in range(k):
    print('Building stamp {}'.format(front_color))
    stamps.append(Stamp(front_design, back_design, mask, front_color, front_raise = 60, back_raise = 15, center = 180))
    stamps[-1].save('stamp{}.stl'.format(front_color))



CR = ComponentResolver(kbase)
for ii in range(k):
    color = next(iter(CR.components_by_color[-1][0].boundarycolors))
    
    stencil = Stencil(CR.base, CR.base.colors[color])
    stencil.show()
    
    CR.color_to_mask(color)
