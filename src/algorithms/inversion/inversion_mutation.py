import random


class InversionMutation:
    def __init__(self, mutation_rate):
        self.mutation_rate = mutation_rate

    def inversion_mutation(self, specimen1):
        mutated_specimen = []

        for i in range(len(specimen1.specimen)):
            chromosome = specimen1.specimen[i].chromosome

            mutated_chromosome1 = chromosome[:]

            if random.random() < self.mutation_rate:
                start = random.randint(0, len(chromosome) - 1)
                end = random.randint(start, len(chromosome))
                mutated_chromosome1[start:end] = reversed(chromosome[start:end])

            mutated_specimen.append(mutated_chromosome1)

        return mutated_specimen
