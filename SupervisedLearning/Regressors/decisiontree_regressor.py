class DecisionTreeNode(object):

    """

    """

    def __init__(self, node):
        pass



class DecisionTreeRegressor:

    """
    Decision Trees are non-parametric models that divide the predictor space
    in segments that reduce the Residual Sum of Squares (RSS). 

    Decision Trees follow a top-down greedy approach aka recursive binary splitting.
    It starts from the top of the tree which is a single region of all observatins,
    and the successively splits the predictor space - into two new branches.
    This process is greedy because the best split made at a particular step is achieved
    by without looking ahead.

    All predictors are considered and all possible cutpoint values for each predictor is
    considered, and the predictor and cutpoint is chosen that reduces the RSS the most.

    sum(y_i - ymean_region1)**2  + sum( y_i  - ymean_region2) **2
    continue process until a stopping criterion is reached

    Methods to deal with ovefitting - Tree pruning - make the trees smaller

    """