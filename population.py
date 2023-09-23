import individual

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
            print(self.inds[i].chromosome)
    ##########################################################################