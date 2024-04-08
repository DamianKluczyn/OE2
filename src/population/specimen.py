from .chromosome import Chromosome
from typing import Tuple, List


class Specimen:
    def __init__(self, number_of_chromosomes: int, boundries: Tuple[float, float], accuracy: int):
        self.number_of_chromosomes = number_of_chromosomes
        self.specimen = [Chromosome(boundries, accuracy) for _ in range(number_of_chromosomes)]

    def get_number_of_chromosomes(self) -> int:
        return self.number_of_chromosomes

    def get_specimen(self) -> List[Chromosome]:
        return self.specimen

    def __str__(self) -> str:
        result = 'Specimen:\n'
        for chromosome in self.specimen:
            result += f'\t{chromosome.__str__()}'
        return f'{result}\n'


