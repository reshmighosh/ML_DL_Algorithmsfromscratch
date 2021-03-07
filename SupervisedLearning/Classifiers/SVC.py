from utils.metrics_loss import *
import numpy as np
import math


class SVC(object):

    """
    Support Vector Machine algorithm tries to fit in a widest possible
    margin between two classes, and also ensures to keep the widest
    possible distance between two extreme points of the two classes.

    For multi-class SVM classification - one vs all technique is commonly
    used to fit in a separate classifier for each class label distinguing
    it from all other class labels.

    Hard Margin: Data has to be linearly separable; sensitive to outliers
    """