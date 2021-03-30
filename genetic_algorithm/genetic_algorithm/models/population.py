import random
from chromossome import Chromossome


class Population:
    def __init__(self, n_chromossomes):
        self.chromossomes = self.generate_initial_chromossomes(n_chromossomes)
        self.population_size = n_chromossomes

    def generate_initial_chromossomes(n_chromossomes):
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

        for chromossome in self.chromossomes[1:-1]:
            if chromossome.fit < best_chromossome.fit:
                best_chromossome = chromossome

        return best_chromossome

    def worst_fit(self):
        worst_chromossome = self.chromossomes[0]

        for chromossome in self.chromossomes[1:-1]:
            if chromossome.fit > best_chromossome.fit:
                best_chromossome = chromossome

        return best_chromossome

    def average_fit(self):
        total_fit = 0

        for chromossome in self.chromossomes:
            total_fit += chromossome.fit

        return total_fit/self.population_size

    def tournment(self):
        pop_index = list(range(self.population_size))
        parents = []
        chromossome = random.randomint(pop_size)
        parents = parents.append(self.chromossomes[pop_index.pop(chromossome)])
        chromossome = random.randomint(pop_size - 1)
        parents = parents.append(self.chromossomes[pop_index.pop(chromossome)])

        if parents[0].fit < parents[1].fit:
            return parents[0]

        return parents[1]

    def crossover(self):
        cross_index = 0.6
        slices = 2
        parents = []
        while count(parents) < 2:
            parent = self.tournment()
            if parent not in parents:
                parents.append(parent)

        if random.random() > cross_index:
            return parents

        children = ['', '']
        slices = random.randomint(1, len(parents[0].genes), slices)
        slices.insert(0, 0)
        slices.insert(-1, -1)

        for i in range(len(slices) - 1):
            children[0] = ''.join(
                children[0],
                parents[i%2].genes[slices[i]:slices[i+1]])
            children[1] = ''.join(
                children[1],
                parents[(i+1)%2].genes[slices[i]:slices[i+1]])

        children[0] = Chromossome(children[0]).mutation()
        children[1] = Chromossome(children[1]).mutation()

        return children


    def reproduction(self):
        best_chromossome = self.best_fit()
        new_chromossomes = []

        while len(new_chromossomes) < self.population_size:
            new_chromossomes += self.crossover()

        new_chromossomes.append(best_chromossome)
        new_chromossomes.remove(self.worst_fit())
        self.chromossomes = new_chromossomes
