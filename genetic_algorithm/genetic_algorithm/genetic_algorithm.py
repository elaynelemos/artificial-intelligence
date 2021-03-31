from genetic_algorithm.models.population import Population


def genetic_algorithm(n_generations):
    population = Population(4)
    generations = []

    while len(generations) < n_generations and not kept_fit(generations):
        generations.append(population)
        print_generation(len(generations), population)

        population.reproduction()

    generations.append(population)
    print_generation(len(generations), population)
    solution = generations[-1].best_fit().value()
    print(f'Solution: f({solution}) = {generations[-1].best_fit().fit}')

    return solution


def kept_fit(generations):
    average_fits = []
    best_fits = []

    if len(generations) < 5:
        return False

    for generation in generations:
        average_fits.append(generation.average_fit())
        best_fits.append(generation.best_fit())

    init = len(generations) - 5
    average = average_fits[init]
    best = best_fits[init]
    for i in range(init + 1, len(average_fits)):
        if average_fits[i] != average:
            average = None
        if best != best_fits[i]:
            best = None
        if average is None and best is None:
            return False

    return True


def print_generation(gen_index, generation):
    chromossomes_genes = []
    chromossomes = generation.chromossomes

    for i in range(len(chromossomes)):
        chromossomes_genes.append(
            f"Chromossome {i + 1} '{chromossomes[i].genes}' = "
            f'{chromossomes[i].value()}')

    output = '\n'.join(chromossomes_genes)
    print(f'Generation #{gen_index}')
    print(output)


if __name__ == '__main__':
    genetic_algorithm(10)
