#from algorithms.crossover import crossover
#from algorithms.mutation import mutation
#from algorithms.selection import selection
#from configuration import config
#from utilities import generating_files
#from optimization import optimization
#from population import Chromosome
from src.configuration.config import Config
from src.population.population import Population

if __name__ == '__main__':
    config = Config()
    population = Population(3, 3, (-10, 10), 6)
    print(population)

