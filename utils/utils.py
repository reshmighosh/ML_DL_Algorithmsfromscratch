import numpy as np
import math
import sys

"""

Basic operations for loss calculaions

"""

def  variance(X):
    "Returns the variance of the features in X"
    mean = np.ones(X.shape) * X.mean(0)
    num_samples = 1/X.shape[0]
    variance = n_samples * np.diag((X - mean).T.dot(X - mean))
    return variance

def std(X):
    " Returns the standard deviations of the features in dataset X"
    std = math.sqrt(variance(X))
    return std

"""
Loss functions for various ML algorithms

"""

def mse(y_observed, y_predicted):
    "Returns the mse between observed values of y and predicted values"
    mse = np.mean((y_observed - y_predicted)**2)
    return mse

def rmse(y_observed, y_predicted):
    "Returns the root mse between observed values of y and predicted values"
    return math.sqrt(mse(y_observed, y_predicted))

def cross_entropy(X):
    # Implement when you have time
    pass

