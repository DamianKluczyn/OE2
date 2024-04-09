from .chromosome import Chromosome
from typing import Tuple, List
from src.optimization.optimization import Optimization


class Specimen:
    def __init__(self, number_of_chromosomes: int, boundries: Tuple[float, float], accuracy: int, fitness_function: str):
        self.number_of_chromosomes = number_of_chromosomes
        self.specimen = [Chromosome(boundries, accuracy) for _ in range(number_of_chromosomes)]
        self.fitness_function = fitness_function
        self.fitness = None
        self.calculate_fitness()

    def get_number_of_chromosomes(self) -> int:
        return self.number_of_chromosomes

    def get_specimen(self):
        return self.specimen

    def get_decoded_specimen(self):
        return [x.decode_binary_chromosome() for x in self.specimen]

    def get_fitness(self):
        return self.fitness

    def calculate_fitness(self):
        optimization = Optimization()
        if self.fitness_function == "Bent Cigar":
            self.fitness = optimization.bent_cigar_function(self.get_decoded_specimen())
        elif self.fitness_function == "Hypersphere":
            self.fitness = optimization.hypersphere(self.get_decoded_specimen())

    def __str__(self) -> str:
        result = 'Specimen:\n'
        for chromosome in self.specimen:
            result += f'\t{chromosome.__str__()}'
        return f'{result}, \t{self.fitness}\n'


