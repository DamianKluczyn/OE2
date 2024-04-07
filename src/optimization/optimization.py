import numpy as np

class Optimization:
    def __init__(self):
        pass

    @staticmethod
    def bent_cigar_function(x):
        return x[0]**2 + 10**6 * np.sum(xi**2 for xi in x[1:])

    @staticmethod
    def de_jong_3(x):
        return np.sum(np.floor(x))
