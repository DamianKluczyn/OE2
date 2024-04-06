import numpy as np
import random


class Crossover:
    def __init__(self, crossover_prob=0.9):
        self.crossover_prob = crossover_prob

    def single_point_crossover(self, chromosome_1, chromosome_2):
        if random.random() < self.crossover_prob:
            point = random.randint(1, len(chromosome_1) - 2)
            child_1 = np.concatenate((chromosome_1[:point], chromosome_2[point:]))
            child_2 = np.concatenate((chromosome_2[:point], chromosome_1[point:]))
            return child_1, child_2
        return chromosome_1, chromosome_2

