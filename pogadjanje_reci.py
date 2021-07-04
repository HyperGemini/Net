import string
import random


class Chromosome:
    def __init__(self, genetic_code, fitness):
        self.genetic_code = genetic_code
        self.fitness = fitness

    def __repr__(self):
        return str(self)

    def __str__(self):
        return "{} = {}".format(''.join(self.genetic_code), self.fitness)


class GeneticAlgorithm:
    def __init__(self, target):
        self.target = target
        self.possible_gene_values = string.ascii_letters
        
        self.chromosome_size = len(target)
        self.generation_size = 5000
        self.reproduction_size = 1000
        self.mutation_rate = 0.1
        self.tournament_size = 10
        self.max_iterations = 1000
        self.selection_type = self.roulette_selection


    def calculate_fitness(self, genetic_code):
        fitness_value = 0

        for i in range(self.chromosome_size):
            if genetic_code[i] == self.target[i]:
                fitness_value += 1

        return fitness_value


    def initial_population(self):
        init_population = []

        for _ in range(self.generation_size):
            genetic_code = random.choices(self.possible_gene_values, k=self.chromosome_size)
            fitness = self.calculate_fitness(genetic_code)
            new_chromozome = Chromosome(genetic_code, fitness)
            init_population.append(new_chromozome)

        return init_population


    def roulette_selection(self, population):
        winner = random.choices(population, weights=[p.fitness for p in population], k=1)
        return winner[0]


    def tournament_selection(self, population):
        selected = random.sample(population, self.tournament_size)
        winner = max(selected, key=lambda x: x.fitness)
        return winner


    def selection(self, population):
        result = [self.selection_type(population) for _ in range(self.reproduction_size)]
        return result


    def crossover(self, parent1: Chromosome, parent2: Chromosome):
        break_point = random.randint(1, self.chromosome_size)
        child1 = parent1.genetic_code[:break_point] + parent2.genetic_code[break_point:]
        child2 = parent2.genetic_code[:break_point] + parent1.genetic_code[break_point:]

        return child1, child2

    
    def mutate(self, genetic_code):
        random_value = random.random()

        if random_value < self.mutation_rate:
            random_index = random.randrange(len(genetic_code))
            genetic_code[random_index] = random.choice(self.possible_gene_values)
        
        return genetic_code


    def create_generation(self, population):
        generation = []
        generation_size = 0

        while generation_size < self.generation_size:

            # Proizvoljno biramo 2 roditelja
            parents = random.sample(population, 2)

            # Dobijamo 2 deteta ukrstanjem
            child1, child2 = self.crossover(parents[0], parents[1])

            # Vrsi se mutacija nad decom
            child1 = self.mutate(child1)
            child2 = self.mutate(child2)

            # Pravimo nove hromozome
            child1 = Chromosome(child1, self.calculate_fitness(child1))
            child2 = Chromosome(child2, self.calculate_fitness(child2))

            # Dodajemo u generaciju
            generation.append(child1)
            generation.append(child2)

            generation_size += 2

        return generation

    
    def optimize(self):
        population = self.initial_population()

        for i in range(self.max_iterations):
            selected = self.selection(population)
            population = self.create_generation(selected)

            best_chromozome = max(population, key=lambda x: x.fitness)
            print(best_chromozome)

            if best_chromozome.fitness == self.chromosome_size:
                break

        return best_chromozome


if __name__ == '__main__':
    genetic_algorithm = GeneticAlgorithm('NKnInJNJVhivIHVhGVtuCtyTuf')
    solution = genetic_algorithm.optimize()
    print(f"Solution: {solution}")
    