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
    # fitness function poczatkowe + zapis do pliku nr. 0 epoki
    print(f"Initial population: {population}")

    start_time = time.time()

    for epoch in range(number_of_epochs):
        # poczatkowa pop = 20
        # selection = GeneticSelection(...) # dostaje populacje zwraca liste osobnikow wybranych (tournament_size)

        # elite = Elite(...) # przyjmuje populacje z selection, zwraca x osobnikow odrazu do nowej populacji

        # new_population = populacja z selection - indeksy elit (liczba osobikow: np. 10 - 2 osobniki)

        # 8
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


if __name__ == '__main__':
    # config = Config()
    # population = Population(3, 3, (-10, 10), 6)
    # print(population)

    app = gui.GUIClass()
    app.mainloop()

"""
Populacja na wiele osbonikow
Osobnik ma wiele chromosomow i ich fitness function dwie tablice: 1. binarna, 2. fitness(x,y)
x - zdekodowany binarny chromosom
y - wartosc fitness

Selekcja przyjmuje populacje
iteruje po osobnikach wybierając osobnika z najlepszym min/max

"""
