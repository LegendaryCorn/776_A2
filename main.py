import genetic_algorithm as ga
import numpy as np
import eval_dejong1 as ev1

##########################################################################  
# The main function
def main():
    #np.random.seed(1)
    
    ##########################################
    # Params needs to be array size 4
    # Population Size
    # Generation Count
    # Crossover Probability
    # Mutation Probability
    params = [50, 75, 0.667, 0.01]
    ##########################################

    gen_algo = ga.GeneticAlgorithm(ev1.EvaluatorDeJong1(), params)
    gen_algo.run_sga()

##########################################################################  

##########################################################################  
if __name__ == "__main__":
    main()
##########################################################################  