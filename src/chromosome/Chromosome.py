import numpy as np
from typing import Tuple, List
from math import log2, ceil


class Chromosome:
    def __init__(self, boundaries: Tuple[float, float], accuracy: int):
        self.boundaries = boundaries
        self.accuracy = accuracy
        self.chromosome_length = ceil(log2((boundaries[1] - boundaries[0]) * 10 ** accuracy))
        self.chromosome = np.random.choice([0, 1], size=self.chromosome_length, p=[0.5, 0.5])

    def return_boundaries(self):
        return self.boundaries

    def return_accuracy(self):
        return self.accuracy

    def return_chromosome_length(self):
        return self.chromosome_length

    def return_chromosome(self):
        return self.chromosome

    def decode_binary_chromosome(self):
        decimal = sum(value * (2 ** index) for index, value in enumerate(reversed(self.chromosome)))
        return (self.boundaries[0] + decimal *
                (self.boundaries[1] - self.boundaries[0]) / (2 ** self.chromosome_length - 1))

