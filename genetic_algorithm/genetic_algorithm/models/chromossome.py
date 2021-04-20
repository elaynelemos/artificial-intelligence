import random


class Chromossome:
    def __init__(self, genes):
        self.genes = genes
        self.fit = self.fitness()

    def __twos_complement(self, val, bits):
        val = int(val, 2)
        if (val & (1 << (bits - 1))) != 0:
            val = val - (1 << bits)
        return val

    def is_valid(self):
        value = self.__twos_complement(self.genes, 5)
        if value < 0:
            value = value*(-1)

        return value <= 10

    def value(self):
        return self.__twos_complement(self.genes, 5)

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
