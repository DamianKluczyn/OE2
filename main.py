from src.algorithms.crossover import crossover
from src.algorithms.mutation import mutation
from src.algorithms.selection import selection
from src.configuration import config
from src.utilities import generating_files
from src.optimization import optimization
from src.population import chromosome
from src.configuration.config import Config
from src.population.population import Population
from src.gui import gui

import time


def main_function():
    config = Config()

    start_range = config.get_param('algorithm_parameters.start_range_a', -10)
    end_range = config.get_param('algorithm_parameters.end_range_b', 10)
    population_size = config.get_param('algorithm_parameters.population_size', 20)
    binary_precision = config.get_param('algorithm_parameters.binary_precision', 6)
    number_of_variables = config.get_param('algorithm_parameters.number_of_variables', 10)
    number_of_epochs = config.get_param('algorithm_parameters.number_of_epochs', 50)

    population = Population(population_size, number_of_variables, (start_range, end_range), binary_precision)
    print(f"Initial population: {population}")

    start_time = time.time()

    for epoch in range(number_of_epochs):
        # selection = GeneticSelection(...)
        # offspring = selection.select(population)
        # crossover = Crossover(...)
        # mutated_offspring = Mutation(...)
        # population.update(mutated_offspring)

        print(f"Epoch {epoch + 1}/{number_of_epochs} completed.")

    end_time = time.time()
    exec_time = end_time - start_time
    print(f"Algorithm finished in {exec_time} seconds.")


if __name__ == '__main__':
    # config = Config()
    # population = Population(3, 3, (-10, 10), 6)
    # print(population)
    app = gui.GUIClass()
    app.mainloop()

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
