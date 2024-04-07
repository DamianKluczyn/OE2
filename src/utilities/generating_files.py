import matplotlib.pyplot as plt

class DataSaver:
    def __init__(self):
        pass

    def plot_and_save(self, data, title, filename):
        generations = list(range(1, len(data) + 1))
        plt.plot(generations, data)
        plt.xlabel("Generation number")
        plt.ylabel("Best")
        plt.title(title)
        plt.grid(True)
        plt.savefig(filename)
        plt.show()

    def save_to_file(self, data, filename):
        with open(filename, 'w') as file:
            for i, item in enumerate(data, 1):
                file.write(f"{i}: {item}\n")

# Przykładowe użycie klasy
# data = [10, 8, 6, 4, 2, 1, 3, 5, 7, 9]
# plotter = DataPlotter()
# plotter.plot_and_save(data, title="Best Chromosome Evolution", filename="best_chromosome_evolution.png")
# plotter.save_to_file(data, filename="best_chromosome_evolution.txt")
