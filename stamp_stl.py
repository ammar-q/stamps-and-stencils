STL_UNIT = 0.1
def stamp_stl(front_design, back_design, front_color, back_color, mask, front_raise = 16, back_raise = 4, center = 4):
    dimx, dimy = reduce((lambda a, b : (min(a[0], b[0]),min(a[1], b[1]))), (ar.shape for ar in (front_design, back_design, mask)))
    stamp = []
    for ii in range(dimx):
        for jj in range(dimy):
            if mask[ii][jj]:
                b = 0
                if back_design[ii][jj] == back_color:
                    b = back_raise   
                l = center + b
                if front_design[ii][jj] == front_color:
                    l += front_raise
                
                o = [ii, jj, -b]
                stamp.append(cube_mesh(origin = o, scale = [1, 1, l]))
    return join_meshes(stamp)

def cube_mesh(origin, scale = [1, 1, 1]):



def join_meshes(list_of_meshes):
