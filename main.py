# from algorithms.crossover import crossover
# from algorithms.mutation import mutation
# from algorithms.selection import selection
# from configuration import config
# from utilities import generating_files
# from optimization import optimization
# from population import Chromosome
from src.configuration.config import Config
from src.population.population import Population

import time


# TODO klasa populacja, klasa osobnik, klasa fitness function

def main_function():
    start_time = time.time()
    time.sleep(5)
    end_time = time.time()
    return end_time - start_time


if __name__ == '__main__':
    config = Config()
    population = Population(3, 3, (-10, 10), 6)
    print(population)

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
