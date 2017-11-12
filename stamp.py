import numpy as np
from stl import mesh
from functools import reduce

class Stamp:
    def __init__(self, front_design, back_design, mask, front_color, front_raise = 16, back_raise = 4, center = 4):
        dimx, dimy = reduce((lambda a, b : (min(a[0], b[0]),min(a[1], b[1]))), ((ar.dimx, ar.dimy) for ar in (front_design, back_design, mask) if ar))
        meshes = []
        for ii in range(dimx):
            for jj in range(dimy):
                if not mask or mask[ii][jj][-1]:
                    b = 0
                    if back_design:
                        b = back_raise * (back_design[ii][jj][-1]/255)   
                    l = center + b
                    if front_design[ii][jj] == front_color:
                        l += front_raise * (front_design.base[ii][jj][-1]/255)   
                    
                    o = [ii, jj, b-l]
                    meshes.append(cube(origin = o, scale = [1, 1, l]))
        self.mesh = join_meshes(meshes)

    def save(self, filename):
        self.mesh.save(filename)



STL_UNIT = 0.1

# Sourced from numpy-stl documentation
def cube(origin, scale):
    # Define the 8 vertices of the cube
    vertices = np.array([[0, 0, 0], [1, 0, 0], [1, 1, 0], [0, 1, 0], [0, 0, 1], [1, 0, 1], [1, 1, 1], [0, 1, 1]])
    # Define the 12 triangles composing the cube
    faces = np.array([[0,3,1], [1,3,2], [0,4,7], [0,7,3], [4,5,6], [4,6,7], [5,1,2], [5,2,6], [2,3,6], [3,7,6], [0,1,5], [0,5,4]])
    # Create the mesh
    cube = mesh.Mesh(np.zeros(faces.shape[0], dtype=mesh.Mesh.dtype))
    for i, f in enumerate(faces):
        for j in range(3):
            cube.vectors[i][j] = (vertices[f[j],:]*scale + origin)*STL_UNIT

    return cube
    
# Sourced from stack overflow "https://stackoverflow.com/questions/43957780/how-to-save-multiple-meshes-in-python-using-numpy-stl"
def join_meshes(meshes):
    total_length_data = 0
    for i in range(len(meshes)):
        total_length_data += len(meshes[i].data)

    data = np.zeros(total_length_data, dtype = mesh.Mesh.dtype)
    data['vectors'] = np.array(meshes).reshape((-1, 9)).reshape((-1, 3, 3))
    return mesh.Mesh(data.copy())

