import random


class Mutation:
    def __init__(self, mutation_rate):
        self.mutation_rate = mutation_rate

    def boundary_mutation(self, specimen):
        mutated_specimen = specimen.copy()

        for chromosome_index, chromosome in enumerate(mutated_specimen):
            for gene_index, gene in enumerate(chromosome):
                if random.random() < self.mutation_rate:
                    mutated_specimen[chromosome_index][gene_index] = 1 - gene

        return mutated_specimen

    def one_point_mutation(self, specimen):
        mutated_specimen = specimen.copy()

        for chromosome_index, chromosome in enumerate(mutated_specimen):
            if random.random() < self.mutation_rate:
                point = random.randint(0, len(chromosome) - 1)
                mutated_specimen[chromosome_index][point] = 1 - chromosome[point]

        return mutated_specimen

    def two_point_mutation(self, specimen):
        mutated_specimen = specimen.copy()

        for chromosome_index, chromosome in enumerate(mutated_specimen):
            if random.random() < self.mutation_rate:
                points = random.sample(range(len(chromosome)), 2)
                points.sort()

                for i in range(points[0], points[1]+1):
                    mutated_specimen[chromosome_index][i] = 1 - chromosome[i]

        return mutated_specimen
