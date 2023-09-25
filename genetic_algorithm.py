import population
import individual
import numpy as np

class GeneticAlgorithm:
    
    ##########################################################################     
    def __init__(self, eval, params):
        self.eval = eval
        self.pop = population.Population()
        
        self.pop_size = params[0]
        self.gen_count = params[1]
        self.p_cross = params[2]
        self.p_mut = params[3]
    ########################################################################## 

    ########################################################################## 
    # Main loop of the Simple GA    
    def run_sga(self):

        # Initialize
        self.pop.random_generate_individuals(self.pop_size, self.eval.get_chrom_len())
        self.pop.eval_pop(self.eval)
        self.record_pop(self.pop) # Should record the initial population

        # Generation loop
        for i in range(self.gen_count):
            pop_new = self.pop.generate_children(self.p_cross, self.p_mut)
            pop_new.eval_pop(self.eval)
            self.pop = pop_new
            self.record_pop(pop_new)

    ##########################################################################

    ########################################################################## 
    # Main loop of the CHC GA   
    def run_chc(self):

        # Initialize
        self.pop.random_generate_individuals(self.pop_size, self.eval.get_chrom_len())
        self.pop.eval_pop(self.eval)
        self.record_pop(self.pop) # Should record the initial population

        # Generation loop TODO
        for i in range(self.gen_count):
            pop_new = self.pop.generate_children(self.p_cross, self.p_mut)
            pop_new.eval_pop(self.eval)
            self.pop = self.chc(self.pop, pop_new)
            self.record_pop(pop_new)

    ##########################################################################

    ########################################################################## 
    # The CHC function  
    def chc(self, pop_old, pop_new):
        pop_chc = population.Population()
        ind_all = []
        fit_all = []

        # Array of all individuals and fitnesses
        for ind_old in pop_old.inds:
            ind_copy = individual.Individual(len(ind_old.chromosome), ind_old.chromosome)
            ind_copy.fitness = ind_old.fitness
            ind_all.append(ind_copy)
            fit_all.append(ind_copy.fitness)
        for ind_new in pop_new.inds:
            ind_copy = individual.Individual(len(ind_new.chromosome), ind_new.chromosome)
            ind_copy.fitness = ind_new.fitness
            ind_all.append(ind_copy)
            fit_all.append(ind_copy.fitness)

        arg_best = np.flip(np.argsort(fit_all))

        for i in range(int(len(arg_best)/2)):
            pop_chc.inds.append(ind_all[arg_best[i]])

        return pop_chc

    ##########################################################################        

    ########################################################################## 
    # Records GA data
    def record_pop(self, pop_to_record):
        min_fit = float('inf')
        max_fit = 0.0
        sum_fit = 0.0
        count = 0.0

        for ind in pop_to_record.inds:
            min_fit = min(ind.fitness, min_fit)
            max_fit = max(ind.fitness, max_fit) 
            sum_fit += ind.fitness
            count += 1

        print(min_fit, sum_fit / count, max_fit)