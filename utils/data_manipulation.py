import numpy as np 
import sys
import os

def standardscaler(X):
    """
    Applies a z-norm transformation to column of interest
    `X: numPy array of dimension (n, X')
    where n = number of rows; X' = number of predictors 
    
    If you use the function over the entire dataset: All
    predictors will be standardized.
    """
    X_copy = X

    mean = np.mean(X, axis = 0)
    std_dev = np.std(X, axis = 0)

    assert len(X.shape) == 2, "Predictors has to be 2-D"
    for predictor in range(X.shape[1]):
        X_copy[:, predictor] = (X_copy[:, predictor] - mean[predictor])/std[predictor]
    return X_copy