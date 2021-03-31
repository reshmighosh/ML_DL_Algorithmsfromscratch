import numpy as np
import math

class kernels():

    def __init__(self, gamma = None, sigma = None, power = None, coef = None):
        self.gamma = gamma
        self.sigma = sigma
        self.power = power
        self.coef = coef

    
    def rbf(self, x, x_1):
        distance = np.power(np.linalg.norm(x - x_1), 2)
        return np.exp(-1*self.gamma*distance)

    def linear_kernel(self, x1, x2):
        return np.inner(x1, x2)
    
    def polynomial_kernel(self, x, x_1):
        p_kernel = np.power((np.inner(x, x1)+ coef), power)
        return p_kernel