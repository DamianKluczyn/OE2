from tkinter import *
from tkinter import ttk
import re


class GUIClass(Tk):
    def __init__(self):
        super().__init__()

        self.resizable(False, False)
        self.title("Obliczenia ewolucyjne - Projekt 2")

        self.create_widgets()

    def create_widgets(self):
        mainframe = ttk.Frame(self, padding="3 3 12 12")
        mainframe.grid(column=0, row=0, sticky="N, W, E, S")
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        vcmd = (self.register(self.validate_entry_data), '%P')
        ivcmd = (self.register(self.on_invalid),)

        ttk.Label(mainframe, text="Begin of the range (a):").grid(column=0, row=0, sticky=W)
        self.begin_range_a = DoubleVar()
        self.begin_range_a_entry = ttk.Entry(mainframe, width=15, textvariable=self.begin_range_a,
                                             validate="focusout", validatecommand=vcmd, invalidcommand=ivcmd)
        self.begin_range_a_entry.grid(column=1, row=0, sticky="N E", padx=5, pady=5)

        ttk.Label(mainframe, text="End of the range (b):").grid(column=0, row=1, sticky=W)
        self.end_range_b = DoubleVar()
        self.end_range_b_entry = ttk.Entry(mainframe, width=15, textvariable=self.end_range_b,
                                           validate="focusout", validatecommand=vcmd, invalidcommand=ivcmd)
        self.end_range_b_entry.grid(column=1, row=1, sticky="N E", padx=5, pady=5)

        ttk.Label(mainframe, text="Size of the population:").grid(column=0, row=2, sticky=W)
        self.pop_size = IntVar()
        self.pop_size_entry = ttk.Entry(mainframe, width=15, textvariable=self.pop_size,
                                        validate="focusout", validatecommand=vcmd, invalidcommand=ivcmd)
        self.pop_size_entry.grid(column=1, row=2, sticky="N E", padx=5, pady=5)

        ttk.Label(mainframe, text="Number of precision bits:").grid(column=0, row=3, sticky=W)
        self.precision_bits = IntVar()
        self.precision_bits_entry = ttk.Entry(mainframe, width=15, textvariable=self.precision_bits,
                                              validate="focusout", validatecommand=vcmd, invalidcommand=ivcmd)
        self.precision_bits_entry.grid(column=1, row=3, sticky="N E", padx=5, pady=5)

        ttk.Label(mainframe, text="Number of epochs:").grid(column=0, row=4, sticky=W)
        self.epochs = IntVar()
        self.epochs_entry = ttk.Entry(mainframe, width=15, textvariable=self.epochs,
                                      validate="focusout", validatecommand=vcmd, invalidcommand=ivcmd)
        self.epochs_entry.grid(column=1, row=4, sticky="N E", padx=5, pady=5)

        ttk.Label(mainframe, text="Best and tournament chromosome amount:").grid(column=0, row=5, sticky=W)
        self.best_chromosome = IntVar()
        self.best_chromosome_entry = ttk.Entry(mainframe, width=15, textvariable=self.best_chromosome,
                                               validate="focusout", validatecommand=vcmd, invalidcommand=ivcmd)
        self.best_chromosome_entry.grid(column=1, row=5, sticky="N E", padx=5, pady=5)

        ttk.Label(mainframe, text="Elite Strategy amount:").grid(column=0, row=6, sticky=W)
        self.elite_strategy = DoubleVar()
        self.elite_strategy_entry = ttk.Entry(mainframe, width=15, textvariable=self.elite_strategy,
                                              validate="focusout", validatecommand=vcmd, invalidcommand=ivcmd)
        self.elite_strategy_entry.grid(column=1, row=6, sticky="N E", padx=5, pady=5)

        ttk.Label(mainframe, text="Cross probability:").grid(column=0, row=7, sticky=W)
        self.crossover_prob = DoubleVar()
        self.crossover_prob_entry = ttk.Entry(mainframe, width=15, textvariable=self.crossover_prob,
                                              validate="focusout", validatecommand=vcmd, invalidcommand=ivcmd)
        self.crossover_prob_entry.grid(column=1, row=7, sticky="N E", padx=5, pady=5)

        ttk.Label(mainframe, text="Mutation probability:").grid(column=0, row=8, sticky=W)
        self.mutation_prob = DoubleVar()
        self.mutation_prob_entry = ttk.Entry(mainframe, width=15, textvariable=self.mutation_prob,
                                             validate="focusout", validatecommand=vcmd, invalidcommand=ivcmd)
        self.mutation_prob_entry.grid(column=1, row=8, sticky="N E", padx=5, pady=5)

        ttk.Label(mainframe, text="Inversion probability:").grid(column=0, row=9, sticky=W)
        self.inversion_prob = DoubleVar()
        self.inversion_prob_entry = ttk.Entry(mainframe, width=15, textvariable=self.inversion_prob,
                                              validate="focusout", validatecommand=vcmd, invalidcommand=ivcmd)
        self.inversion_prob_entry.grid(column=1, row=9, sticky="N E", padx=5, pady=5)

        ttk.Label(mainframe, text="Selection method:").grid(column=0, row=11, sticky=W)
        self.selection_method = StringVar()
        self.selection_method_combo = ttk.Combobox(mainframe, textvariable=self.selection_method)
        self.selection_method_combo['values'] = ("Roulette Wheel", "Tournament", "Select best")
        self.selection_method_combo.grid(column=0, row=12, sticky="N W", padx=5, pady=5)

        ttk.Label(mainframe, text="Crossover method:").grid(column=0, row=13, sticky=W)
        self.crossover_method = StringVar()
        self.crossover_prob_combo = ttk.Combobox(mainframe, textvariable=self.crossover_method)
        self.crossover_prob_combo['values'] = ("Single Point", "Two Point", "Three Point", "Uniform", "Discrete",
                                               "Elite", "Self", "Binary", "Linkage Evolution")
        self.crossover_prob_combo.grid(column=0, row=14, sticky="N W", padx=5, pady=5)

        ttk.Label(mainframe, text="Mutation method:").grid(column=0, row=15, sticky=W)
        self.mutation_method = StringVar()
        self.mutation_method_combo = ttk.Combobox(mainframe, textvariable=self.mutation_method)
        self.mutation_method_combo['values'] = ("Boundary", "One Point", "Two Point")
        self.mutation_method_combo.grid(column=0, row=16, sticky="N W", padx=5, pady=5)

        self.maximization = BooleanVar()
        self.maximization_check = ttk.Checkbutton(mainframe, text="Maximization", variable=self.maximization)
        self.maximization_check.grid(column=0, row=17, sticky=W, padx=5, pady=5)

        self.start_button = ttk.Button(mainframe, text="Start", padding="10 10 10 10", command=self.get_values)
        self.start_button.grid(row=18, padx=5, pady=5, sticky="N E S W")

        self.error_message = ttk.Label(mainframe, foreground="red")
        self.error_message.grid(row=19, padx=5, pady=5, sticky="N E S W")

    def validate_entry_data(self, value):
        patern = r'[+]?([0-9]*[.])?[0-9]+'
        if re.fullmatch(patern, value) is None:
            return False

        return True

    def on_invalid(self):
        self.show_error_message('Please enter a valid value')

    def show_error_message(self, error=''):
        self.error_message['text'] = error

    def get_values(self):
        pass


if __name__ == "__main__":
    app = GUIClass()
    app.mainloop()
