import numpy as np
import random


class Crossover:
    def __init__(self, crossover_prob=0.9, swap_prob=0.5):
        self.crossover_prob = crossover_prob
        self.swap_prob = swap_prob

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

    def uniform_crossover(self, chromosome_1, chromosome_2):
        if random.random() < self.crossover_prob:
            child_1, child_2 = np.copy(chromosome_1), np.copy(chromosome_2)
            mask = [0] * len(chromosome_1)

            for i in range(len(chromosome_1)):
                if random.uniform(0, 1) < self.swap_prob:
                    mask[i] = 1

            for i in range(len(chromosome_1)):
                if mask[i] == 1:
                    child_1[i] = chromosome_1[i]
                    child_2[i] = chromosome_2[i]
                else:
                    child_1[i] = chromosome_2[i]
                    child_2[i] = chromosome_1[i]

            return child_1, child_2
        return chromosome_1, chromosome_2

    # Returns only 1 child!
    def discrete_crossover(self, chromosome_1, chromosome_2):
        if random.random() < self.crossover_prob:
            child_1 = np.copy(chromosome_1)

            for i in range(len(chromosome_1)):
                if random.uniform(0, 1) < self.swap_prob:
                    child_1[i] = chromosome_1[i]
                else:
                    child_1[i] = chromosome_2[i]

            return child_1
        return chromosome_1

    def elite_crossover(self, chromosome_1, chromosome_2):
        if random.random() < self.crossover_prob:
            child_1, child_2 = self.single_point_crossover(chromosome_1, chromosome_2)
            ratings = [sum(chromosome) for chromosome in [chromosome_1, chromosome_2, child_1, child_2]]
            elite_index = np.argsort(ratings)[-2:]
            new_population = [chromosome_1, chromosome_2, child_1, child_2][elite_index[0]], [chromosome_1, chromosome_2, child_1, child_2][elite_index[1]]
            return new_population
        return chromosome_1, chromosome_2

    # Returns only 1 child!
    def self_crossover(self, chromosome_1):
        if random.random() < self.crossover_prob:
            child_1 = np.zeros_like(chromosome_1)
            ones_counter = chromosome_1.count(1)
            ones_index = random.sample(range(len(chromosome_1)), ones_counter)
            for index in ones_index:
                child_1[index] = 1
            return child_1
        return chromosome_1




