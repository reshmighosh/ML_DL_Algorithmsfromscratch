## Pearson's correlation coefficient upto two decimal points


import math

class pearson_correlation:
    
    def __init__(self,list1, list2): ## input data could be of the form of an numpy array as well or any other data structure (even Pandas series)
        self.list1 = list1
        self.list2 = list2

    def correlation(self): 
        n = len(self.list1) 
        x_1 = sum(self.list1) 
        y_1 = sum(self.list2)
        x1_2 = x_1**2
        y1_2 = y_1**2
        x_2 = sum(list(map(lambda x: x**2, self.list1)))
        y_2 = sum(list(map(lambda x: x**2, self.list2)))
        xy = sum(list(map(lambda x, y: x*y, self.list1, self.list2)))
    
        correlation_Numerator = n*xy - (x1 * y1)
        correlation_Denominator = math.sqrt((n*x2) - (x1_2)) * math.sqrt((n*y2) - (y1_2))
        return round(correlation_Numerator/correlation_Denominator, 2)
