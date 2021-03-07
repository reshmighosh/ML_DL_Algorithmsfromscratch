import numpy as np

class XGboost:

    """
    Distributed Gradient Boosting Machine model. Residuals generated from the 
    first trained classifier is used train the next classifier. The objective is
    to minimize the residuals
    """