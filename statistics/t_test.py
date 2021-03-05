import numpy as np
import math

"""
Basics: P value, in hypothesis testing, is the probability of obtaining test results as extreme the results actually observed, when the null hypothesis is considered to be True.

Type 1 error: Basically False Positive - Null hypothesis is true but is incorrectly rejected
Type 2 error: False Negatives: Null hypothesis is actually false but is incorrectly accepted

Significance level or alpha: Probability of rejecting null hypothesis; given null hypothesis was assumed to be True.

Power:

"""

class students_ttest:

    """
    A hypothesis test to see if two 'SAMPLES' are drawn from the same population - check
    means of the two samples to see if they are significantly different from each other

    t-statistic and critical value

    """

