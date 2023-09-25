import individual
import numpy as np

class Population:

    ##########################################################################  
    def __init__(self):
        self.inds = []
    ##########################################################################


    ##########################################################################
    # Will randomly generate individuals.
    def random_generate_individuals(self, pop_size):

        self.inds = []

        for i in range(pop_size):
            self.inds.append(individual.Individual(100))
    ##########################################################################

    ##########################################################################
    # Will generate individuals based on a previous population.
    def generate_children(self, p_cross, p_mut):

        new_pop = Population()
        pop_size = len(self.inds)
        total_fitness = 0

        ##########################################
        # Selection
        for ind in self.inds: # Calculating total fitness
            total_fitness += ind.fitness
        
        for i in range(pop_size):
            sum = 0
            sum_to_beat = total_fitness * np.random.random()
            for ind in self.inds:
                sum += ind.fitness
                if sum > sum_to_beat:
                    new_pop.inds.append(individual.Individual(len(ind.chromosome), ind.chromosome))
                    break
        ##########################################

        ##########################################
        # Crossover
        for i in range(pop_size):
            if i % 2 == 1: # We only want every 2 pop members
                continue

            if(np.random.random() < p_cross):
                new_chrom_1 = new_pop.inds[i].chromosome
                new_chrom_2 = new_pop.inds[i+1].chromosome

                for j in range(np.random.randint(pop_size - 1) + 1):
                    new_chrom_1[j] = new_pop.inds[i+1].chromosome[j]
                    new_chrom_2[j] = new_pop.inds[i].chromosome[j]

                new_pop.inds[i].chromosome = new_chrom_1
                new_pop.inds[i+1].chromosome = new_chrom_2
        ##########################################

        ##########################################
        # Mutation
        for i in range(pop_size):
            for j in range(len(new_pop.inds[i].chromosome)):
                if(np.random.random() < p_mut):
                    new_pop.inds[i].chromosome[j] = 1 - new_pop.inds[i].chromosome[j]
        ##########################################

        return new_pop
    ##########################################################################

    ##########################################################################  
    # Evaluates the whole population, gives individuals their fitnesses.
    def eval_pop(self, eval):
        for ind in self.inds:
            ind.fitness = eval.get_fitness(ind.chromosome)
    ##########################################################################