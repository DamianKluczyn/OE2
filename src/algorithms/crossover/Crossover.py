import numpy as np
import random


class Crossover:
    def __init__(self, crossover_prob=0.9):
        self.crossover_prob = crossover_prob

    def single_point_crossover(self, chromosome_1, chromosome_2):
        if random.random() < self.crossover_prob:
            point = random.randint(1, len(chromosome_1) - 2)
            child_1 = np.concatenate((
                chromosome_1[:point],
                chromosome_2[point:]))
            child_2 = np.concatenate((
                chromosome_2[:point],
                chromosome_1[point:]))
            return child_1, child_2
        return chromosome_1, chromosome_2

    def two_point_crossover(self, chromosome_1, chromosome_2):
        if random.random() < self.crossover_prob:
            point_1 = random.randint(1, len(chromosome_1) - 3)
            point_2 = random.randint(point_1 + 1, len(chromosome_1) - 2)
            child_1 = np.concatenate((
                chromosome_1[:point_1],
                chromosome_2[point_1:point_2],
                chromosome_1[point_2:]))
            child_2 = np.concatenate((
                chromosome_2[:point_1],
                chromosome_1[point_1:point_2],
                chromosome_2[point_2:]))
            return child_1, child_2
        return chromosome_1, chromosome_2

    def three_point_crossover(self, chromosome_1, chromosome_2):
        if random.random() < self.crossover_prob:
            points = sorted(random.sample(range(1, len(chromosome_1) - 1), 3))
            child_1 = np.concatenate((
                chromosome_1[:points[0]],
                chromosome_2[points[0]:points[1]],
                chromosome_1[points[1]:points[2]],
                chromosome_2[points[2]:]))
            child_2 = np.concatenate((
                chromosome_2[:points[0]],
                chromosome_1[points[0]:points[1]],
                chromosome_2[points[1]:points[2]],
                chromosome_1[points[2]:]))
            return child_1, child_2
        return chromosome_1, chromosome_2
