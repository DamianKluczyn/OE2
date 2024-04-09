import random

from src.algorithms.inversion.inversion_mutation import InversionMutation
from algorithms.crossover.crossover import Crossover
from algorithms.mutation.mutation import Mutation
from src.algorithms.selection.selection import GeneticSelection
from src.configuration.config import Config
from src.population.population import Population
from src.algorithms.selection.elite import Elite
#from src.gui import gui

import time


def main_function():
    config = Config()

    start_range = config.get_param('algorithm_parameters.start_range_a')
    end_range = config.get_param('algorithm_parameters.end_range_b')
    population_size = config.get_param('algorithm_parameters.population_size')
    binary_precision = config.get_param('algorithm_parameters.binary_precision')
    number_of_variables = config.get_param('algorithm_parameters.number_of_variables')
    number_of_epochs = config.get_param('algorithm_parameters.number_of_epochs')
    fitness_function = config.get_param('algorithm_parameters.fitness_function')
    selection_method = config.get_param('algorithm_parameters.selection_method')
    selection_count = config.get_param('algorithm_parameters.selection_parameters.tournament_size')
    maximum = config.get_param('algorithm_parameters.maximization')
    use_elite = config.get_param('algorithm_parameters.elite_strategy.use_elite_strategy')
    elite_count = config.get_param('algorithm_parameters.elite_strategy.elite_count')
    crossover_prob = config.get_param('algorithm_parameters.crossover_probability')
    crossover_method = config.get_param('algorithm_parameters.crossover_method')
    mutation_prob = config.get_param('algorithm_parameters.mutation_probability')
    inversion_prob = config.get_param('algorithm_parameters.inversion_probability')
    mutation_method = config.get_param('algorithm_parameters.mutation_method')


    population = Population(population_size, number_of_variables, (start_range, end_range), binary_precision, fitness_function)
    start_time = time.time()
    for specimen in population.get_population():
        print(specimen.get_fitness())

    #zapisywanie epoki nr 0 i jej fitness function

    for epoch in range(number_of_epochs):

        selection = GeneticSelection(population=population.get_population(), selection_type=selection_method, tournament_size=selection_count, max=maximum)
        selected_population = selection.get_best_chromosomes()

        if use_elite:
            elites = Elite(population=selected_population, elite_count=elite_count, max=maximum)
            elite_population = elites.select_elite()
            for elite in elite_population:
                selected_population.remove(elite)

        print(f'selected: {selected_population}')

        crossover = Crossover(crossover_prob=crossover_prob, cross_method=crossover_method)
        crossed_population = selected_population.copy()
        while len(crossed_population) < population_size - elite_count:
            parent1, parent2 = random.sample(selected_population, 2)
            child1, child2 = crossover.cross(parent1, parent2)
            crossed_population.append(child1)
            crossed_population.append(child2)

        for i in range(len(crossed_population)):
            mutation = Mutation(mutation_rate=mutation_prob, mutation_method=mutation_method)
            crossed_population[i] = mutation.mutate(crossed_population[i])

        for i in range(len(crossed_population)):
            inversion = InversionMutation(inversion_prob=inversion_prob)
            crossed_population[i] = inversion.inversion_mutation(crossed_population[i])

        crossed_population.extend(elite_population)
        population.set_population(crossed_population)
        population.fit()
        for specimen in population.get_population():
            print(specimen.get_fitness())

        print(f"Epoch {epoch + 1}/{number_of_epochs} completed.")
        # zapis do pliku wynikow po przeleceniu przez fitness function (min/max)

    # wyswietlic znalezione min/max (zaleznie od checkboxa) z wszystkich pokolen
    # wygenerowac wykres na podstawie txt
    end_time = time.time()
    exec_time = end_time - start_time
    print(f"Algorithm finished in {exec_time} seconds.")
