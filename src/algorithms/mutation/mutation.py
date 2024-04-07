import random


class Mutation:
    def __init__(self, mutation_rate):
        self.mutation_rate = mutation_rate

    def boundary_mutation(self, chromosome):
        mutated_chromosome = chromosome[:]
        for i in range(len(chromosome)):
            if random.random() < self.mutation_rate:
                mutated_chromosome[i] = 1 - chromosome[i]
        return mutated_chromosome

    def one_point_mutation(self, chromosome):
        mutated_chromosome = chromosome[:]
        if random.random() < self.mutation_rate:
            point = random.randint(0, len(chromosome) - 1)
            mutated_chromosome[point] = 1 - chromosome[point]
        return mutated_chromosome

    def two_point_mutation(self, chromosome):
        mutated_chromosome = chromosome[:]
        if random.random() < self.mutation_rate:
            points = random.sample(range(len(chromosome)), 2)
            points.sort()
            for i in range(points[0], points[1]+1):
                mutated_chromosome[i] = 1 - chromosome[i]
        return mutated_chromosome


# Przykładowe wywołanie
# mutation_rate = 0.1
# mutation = Mutation(mutation_rate)
# chromosome = [0, 1, 0, 1, 1, 0, 1, 0, 1, 0]
# mutated_boundary = mutation.boundary_mutation(chromosome)

