from utils.metrics_loss import eucledian_distance
import numpy as np


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
    8. If classification mode of K labels is returned - majority vote

    KNN doesn't have a loss function that needs to be minimized.
    The only training that 


    Parameters:
    -----------
    `k: (int) Number of closest neighbors that will determine/influence
              class of the sample point that we wish to determine
    """
    def __init__(self, k):
        self.k = k

    def majority_vote(self, labels_of_neighbors):
        """
        Return the mode of labels of k top nearest neighbors based on the
        distance metric
        """
        label_counts = np.bincount(labels_of_neighbors.astype('int'))
        assert type(label_of_neighbors) == np.ndarray, "Please make sure the input is a numpy array"
        label_mode_max_idx = label_counts.argmax()
        return label_max_mode_idx

    def predict(self, X_test, X_train, Y_train):

        Y_pred = np.empty(X_test.shape[0])

        # Find the class label of each data point
        for i, element in enumerate(X_test):
            # Sort training examples by their distance to test data point and get K nearest indices
            idx = np.argsort([eucledian_distance(element, x) for x in X_train])[:self.k]

            # Extract labels of K nearest training examples
            knn_labels = np.array([Y_train[i] for i in idx])

            # Label test data point using majority vote - that is most common class in k nearest

            Y_pred[i] = majority_vote(knn_labels)

        return Y_pred
