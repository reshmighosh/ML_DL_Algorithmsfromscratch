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
    variance = num_samples * np.diag((X - mean).T.dot(X - mean))
    return variance

def std(X):
    " Returns the standard deviations of the features in dataset X"
    std = math.sqrt(variance(X))
    return std

def r2_score(y_observed, y_predicted):
    """ Returns the r-squared value; goodness of fit measurement
    R-squared is the statistical measure between 0 and 1 which calculates how
    similar a regression line is to the data it is trying to fit to
    1 - model predicts 100% variance in data
    0 - model predicts none of the variance


    `R-squared is the ratio of variance explained by model to total variance of
    target variable
    SST: Total sum of squares 
    SSE/SSR: Sum of Squared Errors/ Sum of Squared Residuals
    R2 = 1 - SSE/SST
    """
    y_mean = np.mean(y_observed)
    SSE = 0
    SST = 0

    assert len(y_observed) == len(y_predicted), "Number of predictions are not equal to \
        observations"
    for i in range(len(y_observed)):
        SSE += (y_predicted[i] - y_mean)**2
        SST += (y_observed[i] - y_mean)**2

    R2 = 1 - (SSE/SST)
    return R2


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

"""
Distance metrics for various ML algorithms

"""

def eucledian_distance(x1, x2):
    """
    Calculates the eucledian distance or l2 distance between two points
    'x1 and x2 are both array like
    """
    distance = 0
    assert len(x1) == len(x2), "Ensure the length of both arrays or the shape along dimension 0 for two \
                                arrays in comparison is the same"
    for i in range(len(x1)):
        distance.append((x1[i] - x2[i])**2)
    eucledian_distance = math.sqrt(sum(distance))
    return eucledian_distance


