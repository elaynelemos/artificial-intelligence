import random


class Chromossome:
    def __init__(self, genes):
        self.genes = genes
        self.fit = self.fitness()

    def is_valid(self, limit):
        return (int(self.genes[1:-1], 2) < limit)

    def value(self):
        v  = int(self.genes[1:-1], 2)
        if self.genes[0]:
            v  = v*(-1)

        return v

    def fitness(self):
        x = self.value()
        fit = x**2 - 3*x + 4

        return fit

    def mutation(self):
        mutation_rate = 0.01
        genes_len = len(self.genes)

        for i in range(genes_len):
            if random.random() > mutation_rate:
                pass
            self.genes[i] = str((int(chromossome.genes[i]) + 1)%2)

        self.fit = self.fitness()
