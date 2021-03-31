import random


class Chromossome:
    def __init__(self, genes):
        self.genes = genes
        self.fit = self.fitness()

    def is_valid(self):
        return (int(self.genes[1:], 2) <= 10)

    def value(self):
        v  = int(self.genes[1:], 2)
        if self.genes[0] == '1':
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
            bit = '1'
            if self.genes[i] == bit:
                bit = '0'
            self.genes = ''.join([
                self.genes[0:i],
                bit,
                self.genes[i + 1:]])

        self.fit = self.fitness()

        return self
