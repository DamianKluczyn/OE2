from algorithms.crossover import crossover
from algorithms.mutation import mutation
from algorithms.selection import selection
from configuration import config
from utilities import generating_files
from optimization import optimization
from population import Chromosome

#TODO klasa populacja, klasa osobnik, klasa fitness function

if __name__ == '__main__':
    config = config.Config()
    chromosome = Chromosome.Chromosome(
        (config.get_param("algorithm_parameters.start_range_a"),
         config.get_param("algorithm_parameters.end_range_b")),
        config.get_param("algorithm_parameters.binary_precision")
    )


"""
Generowanie populacji
(klasa populacjia, chromosom, osobnik, fitness function(?))

Selekcja (np. z 20 osobnikow 10 zostanie wybranych)

Krzyżowanie - dopóki populacja nie stanie się tak duża jak pierwotna,
losowanie z powtórzeniami
(jak używamy strategii elitarnej to osobniki wybrane przechodzą bez następnych kroków,
20-początkowa, 2-elitarna to 18 trzeba dostać z krzyżowań)

Mutacja

Inwersja

Zakończenie 1 epoki iteracji - 18 osobników z krzyżowania,mutacji,inwersji + 2 z elitarnej

Powtórzenie całości przez daną liczbę epok

"""