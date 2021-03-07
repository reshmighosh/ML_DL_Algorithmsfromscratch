import math
import numpy as np

# Implementing commonly used loss functions in Deep Learning applications


def cross_entropy(y_observed, p):
    """
    Measures the log loss of classifier whose output probability lies between 0
    and 1. XELoss increases as as predicted probability divereges from actual value.
    `p: probability of data belonging to a certain class

    For Binary classification, XELoss is negative of y*log_e(p) + (1-y)log_e(1-p)
    For Multinomial classification, calculate separate loss for each class label per obs
    and add the result
    $\summation over all classes (M-> c= 1...M) y_o,c * log(p_o, c)
    """

    pass


