import numpy as np
from sklearn.cluster import KMeans
from sklearn import datasets

class kPicture:
    def __init__(self, picture, k):
        self.base = picture
        self.k = k
        
        self.dimx, self.dimy = self.base.dimx, self.base.dimy

        # Run k-means clustering
        k_means_filter = KMeans(n_clusters=k, init='k-means++', n_init=5, max_iter=300, tol=0.0001, precompute_distances='auto', verbose=0, random_state=None, copy_x=True, n_jobs=-1, algorithm='auto').fit(picture.im_data)
        
        self.colors =  dict( (ii, k_means_filter.cluster_centers_[ii]) for ii in range(k_means_filter.cluster_centers_))
        self.im = np.array(k_means_filter.labels_).reshape(self.base.dimx, self.base.dimy)
        self.im_data = np.array(k_means_filter.labels_).reshape(-1, 1)
        


def index_opaque(colors):
    return reduce(lambda x,y: x if colors[x][3] > colors[y][3] else y, range(colors))
