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
        k_means_filter = KMeans(n_clusters=k, init='k-means++', n_init=5, max_iter=3000, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=-1, algorithm='auto').fit(picture.im_data()[:,[0,1,2]])
        
        self.colors =  k_means_filter.cluster_centers_
        self.im = np.array(k_means_filter.labels_).reshape(self.dimx, self.dimy)
        

    def __getitem__(self, ii):
        return self.im[ii,:]
        
    def show(self):
        image = Image.fromarray(self.colors[self.im].astype('uint8'), 'RGB')
        image.show()
    
    def im_data(self):
        return np.array(self.im).reshape(self.dimx*self.dimy, -1)

    def add_border(self, thickness, color = -1):
        tmp = np.full((self.dimx, thickness), color)
        self.im = np.hstack((tmp, self.im, tmp))
        tmp = np.full((thickness, self.dimy + 2*thickness), color)
        self.im = np.vstack((tmp, self.im, tmp))
        
        self.dimx = self.dimx + 2*thickness
        self.dimy = self.dimy + 2*thickness
