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


    population = Population(population_size, number_of_variables, (start_range, end_range), binary_precision, fitness_function)

    start_time = time.time()

    for epoch in range(number_of_epochs):

        selection = GeneticSelection(population.get_population(), selection_type=selection_method, tournament_size=selection_count, max=maximum)
        selected_population = selection.get_best_chromosomes()

        if use_elite:
            elites = Elite(selected_population, elite_count, maximum)

            for elite in elites.select_elite():
                selected_population.remove(elite)


        # for i in range(len(population))/2
        #
        # crossover = Crossover(...) # przyjmuje 2 osobniki return dwa osobniki nowe //losowe osobniki
        # new population # nadpisywanie starej populacji skrzyżowanymi len(new) = 18

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
