from algorithms.crossover import crossover
from algorithms.mutation import mutation
from algorithms.selection import selection
from configuration import config
from utilities import generating_files
from optimization import optimization
from population import Chromosome

if __name__ == '__main__':
    config = config.Config()
    chromosome = Chromosome.Chromosome(
        (config.get_param("algorithm_parameters.start_range_a"),
         config.get_param("algorithm_parameters.end_range_b")),
        config.get_param("algorithm_parameters.binary_precision")
    )

