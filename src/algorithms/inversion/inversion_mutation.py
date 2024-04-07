import random


class InversionMutation:
    def __init__(self, mutation_rate):
        self.mutation_rate = mutation_rate

    def inversion_mutation(self, chromosome):
        mutated_chromosome = chromosome[:]

        if random.random() < self.mutation_rate:
            start = random.randint(0, len(chromosome) - 1)
            end = random.randint(start, len(chromosome))
            mutated_chromosome[start:end] = reversed(chromosome[start:end])

        return mutated_chromosome
