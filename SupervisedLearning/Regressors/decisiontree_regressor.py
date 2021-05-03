from utils.metrics_loss import mse, rmse
from utils.metrics_loss import 

class DecisionTreeNode(object):

    """
    Class to recognize decision node (leaf node) and 

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

    ``Algorithm:
        1. Use the top down greedy or recursive binary splitting approach to grow a tree
        until some stopping criterion like terminal node has some min number of obs is 
        achieved
        2. Apply cost complexity pruining to the larger tree to retain small set of sub-trees
        based on the function alpha - hyperparam
        3. Use k-fold CV to choose alpha - divide train datasets on k folds:
            3.1. Repeat steps 1, 2 on k-1 fold and test on k fold and calculate the mse
            on the data for the k fold
            3.2. Avg the mse for each value of alpha and choose alpha to reduce avg mse
        4. Return subtree from step 2 that corresponds to the chosen value of alpha

    
    Versions of decision trees:

    Bagging : Bootstrap aggregating - reduces variances
    builds trees in parallel by using stratified datasets by random sampling using the bootstrap method using replacement
    this means 2/3 rd of the dataset is seen while 1/3 rd of all training examples never appear - out of bag 

    OOB is similar to leave one out cross validation

    Feature importance: record the total amount of RSS that is decreased due to splits over a given predictor and average over all 
    B trees
    for classification  - add total amount of Gini index that is decreased - ue to splits over a given predictor and average over all 
    B trees

    RF - version of bagging - long with random subset of dataset, rf also uses random selection of features, start with sqrt(p)

    Boosting: Trees are grown sequentialy

        1. fit a tree B with d splits (d+1 leaf nodes) to the training data(X,r)
        2. Update the tree by adding a shrunken version of new tree - weight assigned 
        3. update residuals
        4. shrinkage parameter lambda


    AdaBoost: all instances are given equal weights
    1. After the first tree has learnt, the weights are adjusted so that misclassified instances are given more weightage
    2. New model = Tree1+Tree2
    3. Process is repeated and the to predict revised residuals

    Gradient Boosting:
    1. Trains many models in gradual, additive, and sequential manner.
    2. Differs from Adaboost on how the model identifies the shortcomings, latter uses by using high weight
    data points wheres GBM uses gradients of lpss function 

    Hyperparameter tuning for GBM:


    XGBM:
    








    """

