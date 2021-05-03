import numpy as np
import math

class LogisticRegression():

    """
    Logistic Regression uses a sigmoid activation function to
    estimate probabilities logistic function

    log loss = -y(1-p) -(1-y)(1-p)
    

    """

    def __init__(self, learning_rate, gd = None, data):
        self.learning_rate = learning_rate
        self.gd = gd
        self

    def params(self, X):
        num_featurees = X.shape[1]

        

