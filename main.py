import sys
import numpy as np
from picture import *
from kpicture import *
from stamp import *
from stencil import *
from componentresolver import *




# Set main picture
k = int(sys.argv[2])
print('Select main design')
base = Picture()
kbase = kPicture(base, k)

if sys.argv[1] == 'stamp':
    ####################
    #### Stamp flow ####
    ####################

    front_design = kbase

    try:
        print('Select back design')
        back_design = Picture()
    except:
        back_design = None

    try:
        print('Select stamp mask')
        mask = Picture()
    except:
        mask = None

    stamps = []
    for front_color in range(k):
        print('Building stamp {}'.format(front_color))
        stamps.append(Stamp(front_design, back_design, mask, front_color, front_raise = 60, back_raise = 15, center = 180))
        stamps[-1].save('stamp{}.stl'.format(front_color))



if sys.argv[1] == 'stencil':
    ######################
    #### Stencil flow ####
    ######################

    kbase.save('stencil_result.png')
    CR = ComponentResolver(kbase)
    CR.simplify()

    stencils = []
    while CR.num_components():
        stencils.append(Stencil(CR.stencil_component, CR.next_boundary_color()))
        stencils[-1].save('stencil{}.png'.format(len(stencils)))
        CR.grow()
