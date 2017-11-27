import numpy as np
from sklearn.cluster import KMeans
from sklearn import datasets
from functools import reduce
from PIL import Image

class kPicture:
    def __init__(self, picture, k):
        self.base = picture
        self.k = k
        
        self.dimx, self.dimy = self.base.dimx, self.base.dimy

        # Run k-means clustering
        k_means_filter = KMeans(n_clusters=k, init='k-means++', n_init=5, max_iter=3000, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=-1, algorithm='auto').fit(picture.im_data[:,[0,1,2]])
        
        self.colors =  k_means_filter.cluster_centers_
        self.im = np.array(k_means_filter.labels_).reshape(self.dimx, self.dimy)
        

    def __getitem__(self, ii):
        return self.im[ii,:]
        
    def show(self):
        image = Image.fromarray(self.colors[self.im].astype('uint8'), 'RGBA')
        image.show()
    
    def im_data(self):
        return np.array(self.im).reshape(self.dimx*self.dimy, -1)


def index_opaque(colors):
    return reduce(lambda x,y: x if colors[x][3] > colors[y][3] else y, range(len(colors)))

def add_border(kpicture, thickness, color = -1):
    tmp = np.full((kpicture.dimx, thickness), color)
    kpicture.im = np.hstack((tmp, kpicture.im, tmp))
    tmp = np.full((thickness, kpicture.dimy + 2*thickness), color)
    kpicture.im = np.vstack((tmp, kpicture.im, tmp))
    
    kpicture.dimx = kpicture.dimx + 2*thickness
    kpicture.dimy = kpicture.dimy + 2*thickness
