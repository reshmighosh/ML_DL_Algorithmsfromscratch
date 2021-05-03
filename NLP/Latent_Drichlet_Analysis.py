
import spacy
import numpy as np
import nltk
import pandas as np

class LDA(object):

    """
    STEPS in LDA:
    1. For each document, assign each word to one of the k categories(topics) randomly.
    2. For each d go through each word and compute p(topic|document): proportion of words
    in doc d assigned to topic t - excluding the current word
        2.1. If a lot of words belong to t - it is highly probable word w also belongs to 
        topic t
    3. p(word w| topic t): 
    """