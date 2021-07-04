import random

class Chromosome:
    def __init__(self, genetic_code, fitness):
        self.genetic_code = genetic_code
        self.fitness = fitness

    def __str__(self):
        str_ints = [str(i) for i in self.genetic_code]
        return "{} = {}".format(' '.join(str_ints), self.fitness)

    def __repr__(self):
        return str(self)


class GeneticAlgorithm:
    def __init__(self, target_sum, set):
        self.target_sum = target_sum
        self.set = set

        self.chromosome_size = len(self.set)
        self.generation_size = 5000
        self.reproduction_size = 1000
        self.mutation_rate = 0.1
        self.tournament_size = 10
        self.max_iterations = 1000
        self.selection_type = self.tournament_selection

    
    def calculate_fitness(self, chromozome):
        sum = 0

        for i in range(self.chromosome_size):
            sum += self.set[i] * chromozome[i]

        return abs(sum - self.target_sum)
    


    def initial_population(self):
        init_population = []

        for _ in range(self.generation_size):
            genetic_code = random.choices([0, 1], k=self.chromosome_size)
            fitness = self.calculate_fitness(genetic_code)
            new_chromosome = Chromosome(genetic_code, fitness)
            init_population.append(new_chromosome)

        return init_population

    
    def tournament_selection(self, population):
        selected = random.sample(population, self.tournament_size)
        winner = min(selected, key=lambda x: x.fitness)

        return winner


    def selection(self, population):
        result = [self.selection_type(population) for _ in range(self.reproduction_size)]
        return result

    
    def crossover(self, parent_1: Chromosome, parent_2: Chromosome):
        break_point = random.randint(1, self.chromosome_size)
        child_1 = parent_1.genetic_code[:break_point] + parent_2.genetic_code[break_point:]
        child_2 = parent_2.genetic_code[:break_point] + parent_1.genetic_code[break_point:]
        
        return child_1, child_2

    def mutate(self, genetic_code):
        random_value = random.random()

        if random_value < self.mutation_rate:
            random_index = random.randrange(self.chromosome_size)

            if genetic_code[random_index] == 1:
                genetic_code[random_index] = 0
            else:
                genetic_code[random_index] = 1

        return genetic_code

    
    def create_generation(self, population):
        generation = []
        generation_size = 0

        while generation_size < self.generation_size:
            parents = random.sample(population, 2)

            child_1, child_2 = self.crossover(parents[0], parents[1])

            child_1 = self.mutate(child_1)
            child_2 = self.mutate(child_2)

            child_1 = Chromosome(child_1, self.calculate_fitness(child_1))
            child_2 = Chromosome(child_2, self.calculate_fitness(child_2))

            generation.append(child_1)
            generation.append(child_2)

            generation_size += 2

        return generation

    
    def optimize(self):
        population = self.initial_population()

        for _ in range(self.max_iterations):
            selected = self.selection(population)
            population = self.create_generation(selected)

            best_chromozome = min(population, key=lambda x: x.fitness)
            print(best_chromozome)

            if best_chromozome.fitness == 0:
                break

        return best_chromozome


if __name__ == '__main__':
    set = [1, 5, 76, -34, 45, 23, 8, 3]
    target_sum = 34

    genetic_algorithm = GeneticAlgorithm(target_sum, set)
    solution = genetic_algorithm.optimize()

    print(f"Solution: {solution}")
    