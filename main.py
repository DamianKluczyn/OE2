import random

from algorithms.crossover.crossover import Crossover
from src.algorithms.selection.selection import GeneticSelection
from src.configuration.config import Config
from src.population.population import Population
from src.algorithms.selection.elite import Elite
#from src.gui import gui

import time


def main_function():
    config = Config()

    start_range = config.get_param('algorithm_parameters.start_range_a', -10)
    end_range = config.get_param('algorithm_parameters.end_range_b', 10)
    population_size = config.get_param('algorithm_parameters.population_size', 20)
    binary_precision = config.get_param('algorithm_parameters.binary_precision', 6)
    number_of_variables = config.get_param('algorithm_parameters.number_of_variables', 10)
    number_of_epochs = config.get_param('algorithm_parameters.number_of_epochs', 50)
    fitness_function = config.get_param('algorithm_parameters.fitness_function', 'Bent Cigar')
    selection_method = config.get_param('algorithm_parameters.selection_method')
    selection_count = config.get_param('algorithm_parameters.selection_parameters.tournament_size')
    maximum = config.get_param('algorithm_parameters.maximization')
    use_elite = config.get_param('algorithm_parameters.elite_strategy.use_elite_strategy')
    elite_count = config.get_param('algorithm_parameters.elite_strategy.elite_count')
    crossover_prob = config.get_param('algorithm_parameters.crossover_probability')
    crossover_method = config.get_param('algorithm_parameters.crossover_method')


    population = Population(population_size, number_of_variables, (start_range, end_range), binary_precision, fitness_function)
    start_time = time.time()

    for epoch in range(number_of_epochs):

        selection = GeneticSelection(population=population.get_population(), selection_type=selection_method, tournament_size=selection_count, max=maximum)
        selected_population = selection.get_best_chromosomes()

        if use_elite:
            elites = Elite(population=selected_population, elite_count=elite_count, max=maximum)

            for elite in elites.select_elite():
                selected_population.remove(elite)

        print(f'selected: {selected_population}')

        crossover = Crossover(crossover_prob=crossover_prob, cross_method=crossover_method)
        crossed_population = selected_population.copy()
        while len(crossed_population) < population_size - elite_count:
            parent1, parent2 = random.sample(selected_population, 2)
            child1, child2 = crossover.cross(parent1, parent2)
            crossed_population.append(child1)
            crossed_population.append(child2)






        # for i in range(new population)
        # mutation = Mutation(...) # przyjmuje osobnika zwraca osobnika
        # new population (nadpisywanie)

        # for i in range(new population)
        # inversion = Inversion(...) # przyjmuje osobnika zwraca osobnika
        # new population (nadpisywanie)

        # population.update(new population + elite)

        # fitness function

        print(f"Epoch {epoch + 1}/{number_of_epochs} completed.")
        # zapis do pliku wynikow po przeleceniu przez fitness function (min/max)

    # wyswietlic znalezione min/max (zaleznie od checkboxa) z wszystkich pokolen
    # wygenerowac wykres na podstawie txt
    end_time = time.time()
    exec_time = end_time - start_time
    print(f"Algorithm finished in {exec_time} seconds.")
