import random
from genetic_algorithm.models.chromossome import Chromossome


class Population:
    def __init__(self, n_chromossomes):
        self.chromossomes = self.generate_initial_chromossomes(n_chromossomes)
        self.population_size = n_chromossomes

    def generate_initial_chromossomes(self, n_chromossomes):
        binary_values = '01'
        population  = []

        while len(population) < n_chromossomes:
            chromossome  = Chromossome(
                ''.join(random.choice(binary_values) for _ in range(5)))
            if chromossome.is_valid():
                population.append(chromossome)

        return population

    def best_fit(self):
        best_chromossome = self.chromossomes[0]

        for chromossome in self.chromossomes:
            if chromossome.fit < best_chromossome.fit:
                best_chromossome = chromossome

        return best_chromossome

    def worst_fit(self):
        worst_chromossome = self.chromossomes[0]

        for chromossome in self.chromossomes:
            if chromossome.fit > worst_chromossome.fit:
                worst_chromossome = chromossome

        return worst_chromossome

    def average_fit(self):
        total_fit = 0

        for chromossome in self.chromossomes:
            total_fit += chromossome.fit

        return total_fit/self.population_size

    def tournment(self):
        index = random.sample(list(range(self.population_size)), 2)
        parents = [self.chromossomes[index[0]], self.chromossomes[index[1]]]

        if parents[0].fit < parents[1].fit:
            return index[0]

        return index[1]

    def crossover(self):
        cross_index = 0.6
        parents_index = []
        while len(parents_index) < 2:
            index = self.tournment()
            if index not in parents_index:
                parents_index.append(index)

        parents = [
            self.chromossomes[parents_index[0]],
            self.chromossomes[parents_index[1]]]

        if random.random() > cross_index:
            return parents

        children = ['', '']
        slices = random.sample(list(range(1, 4)), 2)
        slices.sort()

        children[0] = ''.join([
            parents[0].genes[0:slices[0]],
            parents[1].genes[slices[0]:slices[1]],
            parents[0].genes[slices[1]:],
        ])
        children[1] = ''.join([
            parents[1].genes[0:slices[0]],
            parents[0].genes[slices[0]:slices[1]],
            parents[1].genes[slices[1]:],
        ])

        children[0] = Chromossome(children[0]).mutation()
        children[1] = Chromossome(children[1]).mutation()

        return children


    def reproduction(self):
        best_chromossome = self.best_fit()
        new_chromossomes = []

        while len(new_chromossomes) < self.population_size:
            new_chromossomes += self.crossover()

        new_chromossomes.append(best_chromossome)
        self.chromossomes = new_chromossomes
        self.chromossomes.remove(self.worst_fit())
