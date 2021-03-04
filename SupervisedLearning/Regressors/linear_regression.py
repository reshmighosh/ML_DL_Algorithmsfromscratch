import numpy as np
import math
import sys
from utils.py import *

class linear_regression(object):
    """
    Linear Regression models data with a linear (staright) line unless splines
    or polynomial predictors are added

    Loss functions include: MSE, RMSE and also analyzed by R-squared, Adjusted 
    R-squared 

    Using Least Squared method the best fitting line is determined by minimizing
    the sum of sqaured error (SSE): sum of squared distance between observations
    and fitted line.
    """

    def __init__(self, predictors, lables):