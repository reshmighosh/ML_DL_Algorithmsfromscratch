class k_nearest: # no need to mention object as new-class style Python3
    """
    K nearest neighbors classifier -
    The KNN classifier assumes that similar things exist in close proximity
    of each other - that is objects from a same class will be near to each
    other.To capture how close objects are to each other a distance metric is
    utilized - distance between two points are calculated

    Choice of distance measures: Eucledian, Manhattan

    Algorithm:
    1. Load the dataset 
    2. Initialize k to choose number of neighbors that will influence your
    class label choice
    3. Iteratively for each data point in your dataset:
        3.1.Calculate the distance between the data point of interest and 
        the current data point under consideration
        3.2. Add the distance and index of the calculation performed above
        in a dictionary
    4. Sort the dictionary in ascending order of distances
    5. Pick the k entries from sorted dictionary
    6. Get the labels of the k entries
    7. If regression (KNN - regressor) mean of the K labels is returned
    8. If classification mode of K labels is returned


    Parameters:
    -----------
    `k: (int) Number of closest neighbors that will determine/influence
              class of the sample point that we wish to determine
    """
    def __init__(self, n )