import genetic_algorithm as ga
import numpy as np

from eval import eval_dejong1 as ev1
from eval import eval_dejong2 as ev2
from eval import eval_dejong3 as ev3
from eval import eval_dejong4 as ev4
from eval import eval_dejong5 as ev5

##########################################################################  
# The main function
def main():
    np.random.seed(1)
    
    ##########################################
    # Params needs to be array size 4
    # Population Size
    # Generation Count
    # Crossover Probability
    # Mutation Probability
    params = [100, 150, 0.9, 0.05]
    ##########################################

    gen_algo = ga.GeneticAlgorithm(ev4.EvaluatorDeJong4(), params)
    gen_algo.run_chc()

##########################################################################  

##########################################################################  
if __name__ == "__main__":
    main()
##########################################################################  