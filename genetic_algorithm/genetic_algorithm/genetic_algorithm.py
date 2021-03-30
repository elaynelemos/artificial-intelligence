from models.population import Population


def genetic_algorithm(n_generations):
    population = Population(4)
    generations = []

    while len(generations) < n_generations and not kept_fit(generations):
        generations.append(population)
        print_generation(population)

        population.reproduction()

    return generations[-1].best_fit().value()


def kept_fit(generations):
    average_fits = []
    best_fits = []

    if len(generations) < 3:
        return False

    for generation in generations:
        average_fits.append(generation.average_fit())
        best_fits.append(generation.best_fit())

    init = len(generations) - 3
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


def print_generation(generation):
    chromossomes_genes = []
    chromossomes = generation.chromossomes

    for i in range(len(chromossomes)):
        chromossomes_genes.append(
            f"Chromossome {i + 1} '{chromossomes[i].genes}' = "
            f'{chromossomes[i].value()}')

    output = '\n'.join(chromossomes_genes)
    print(output)
