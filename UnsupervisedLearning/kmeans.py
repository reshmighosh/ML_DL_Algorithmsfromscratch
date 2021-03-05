import numpy as numpy
import math

class kmeans:

    """
    K-means is an unsupervised learning algorithm to identify clusters
    of patterns in your data - for example recommendation engine

    Inertia: How far the points are from each other within cluster
    i.e. the distance of all points from the centroid of the cluster

    Dunn Index: Distance between two cclisters - the distance between the
    centroids of two different clusters (inter cluster distance) should be
    large
    DunnIndex = min(inter cluster distance)/max(Intra cluster distance)
    maximize DunnIndex

    Objective of kmeans reduce the distance between the points and their 
    respective cluster centroid

    ALgorithm:
            1. Pick the number k, number of clusters
            2. Pick k random points in the predictor space as centroid
            3. Calculate distance between the centroids and all points
            and assign all points closest to cluster centroid to the same
            class
            4. Compute new centroids
            5. Keep repeating 3 and 4 until stopping criteria is met

        Three stopping criteria:
            1. Centroid of newly formed clusters do not change
            2. Points remain the same cluster
            3. Max # of iterations reached


        Challenges:
            2. The  densites of original points are different ie some points are
            closely spaced belonging to one cluster, but other points belonging to 
            other clusters are loosely spaced, hence the algorithm misclassfied

            Fix: increase the number of clusters

    KMeans++ choose initial cluster centroids for kmeans
            1. Pick only one centroid randomly 
            2. Calc distance of all points from this centroid
            3. Choose a new centroid - whose squared distance is farthest from the
            initial centroid. 


            PLot metric (inertia) with accuracy to choose the right number of clusters


    """

    def __init__(self, k):
        self.k = k
    
    def __init__random_centroids(self, X):
        num_samples, n_features = X.shape()
        centroids = np.zeros((self.k, n_features))
        for i in range(self.k):
            
    