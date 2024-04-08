from typing import Tuple, List
from .specimen import Specimen


class Population:
    def __init__(self, population_size: int, number_of_chromosomes_per_specimen: int,
                 boundaries: Tuple[float, float], accuracy: int):
        self.population_size = population_size
        self.population = [Specimen(number_of_chromosomes_per_specimen, boundaries, accuracy)
                           for _ in range(population_size)]

    def get_population_size(self) -> int:
        return self.population_size

    def get_population(self) -> List[Specimen]:
        return self.population

    def __str__(self) -> str:
        result = 'Population:\n'
        for specimen in self.population:
            result += f'\t{specimen.__str__()}'
        return result