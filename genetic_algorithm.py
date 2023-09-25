import population

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
        self.pop.random_generate_individuals(self.pop_size)
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
        self.pop.random_generate_individuals(self.pop_size)
        self.pop.eval_pop(self.eval)
        self.record_pop(self.pop) # Should record the initial population

        # Generation loop TODO
        for i in range(self.gen_count):
            pop_new = self.pop.generate_children(self.p_cross, self.p_mut)
            pop_new.eval_pop(self.eval)
            self.pop = pop_new
            self.record_pop(pop_new)

    ##########################################################################      

    ########################################################################## 
    # Records GA data
    def record_pop(self, pop_to_record):
        print(pop_to_record.inds[0].fitness)    