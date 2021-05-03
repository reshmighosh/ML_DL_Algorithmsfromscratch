import numpy as np
import math

"""
Tree representation - dendogram
Each obs is treated as its own cluster. Two clusters that are similar are fused so that there are 
n-1 clusters
Leaves fuse into branches
Leaves which are closest to one another fuse first and then the rest of the points are analyzed based on
dissimilarity metric.
The earlier/lower the fusion occurs the more similar the observations are
By eye balling an appropriate number of clusters are obtained
Dissimilarity between clusters tells us height at which two clusters should be fused



"""