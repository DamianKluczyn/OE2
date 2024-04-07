import random


class GeneticSelection:
    def __init__(self, population, fitness_function, selection_type='best', tournament_size=2):
        self.population = population
        self.fitness_function = fitness_function
        self.selection_type = selection_type
        self.tournament_size = tournament_size

    def roulette_wheel_selection(self, population):
        fitness_sum = sum(1 / self.fitness_function(chromosome) for chromosome in population)
        probabilities = [1 / (self.fitness_function(chromosome) * fitness_sum) for chromosome in population]
        cumulative_probabilities = [sum(probabilities[:i+1]) for i in range(len(probabilities))]
        random_number = random.uniform(0, 1)
        for i, cum_prob in enumerate(cumulative_probabilities):
            if random_number <= cum_prob:
                return population[i]

    def tournament_selection(self, population, n=1):
        tournament_group = random.sample(population, self.tournament_size)
        best_chromosomes = sorted(tournament_group, key=lambda x: self.fitness_function(x))[:n]
        return best_chromosomes

    def select_best_chromosomes(self, n=1):
        return sorted(self.population, key=lambda x: self.fitness_function(x))[:n]

    def select(self, n=1):
        if self.selection_type == 'best':
            return self.select_best_chromosomes(n)
        elif self.selection_type == 'roulette_wheel':
            return self.roulette_wheel_selection(self.population)
        elif self.selection_type == 'tournament':
            return self.tournament_selection(self.population, n)


# Przykładowe użycie klasy
# def fitness_function(population):
#     return sum(population)
# population_size = 25
# chromosome_length = 3
# population = [[random.randint(0, 9) for _ in range(chromosome_length)] for _ in range(population_size)]
# genetic_algo = GeneticSelection(population, fitness_function, selection_type='best', tournament_size=5)
# selected_chromosomes = genetic_algo.select(n=5)
# print("Selected chromosomes:", selected_chromosomes)
