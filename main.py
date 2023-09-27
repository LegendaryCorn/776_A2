import genetic_algorithm as ga
import numpy as np
import sys

from eval import eval_dejong1 as ev1
from eval import eval_dejong2 as ev2
from eval import eval_dejong3 as ev3
from eval import eval_dejong4 as ev4
from eval import eval_dejong5 as ev5

##########################################################################  
# The main function
def main():

    if(len(sys.argv) != 2):
        print("Invalid arguments. Please enter the appropriate config file.")
        print("python.exe main.py config.txt")
        return
    
    # Read command line input
    f = open(sys.argv[1])
    config = []
    for line in f:
        config.append(float(line.split(" ")[1]))

    # Pick the DeJong function
    eval_list = [ev1.EvaluatorDeJong1(), ev2.EvaluatorDeJong2(), ev3.EvaluatorDeJong3(), ev4.EvaluatorDeJong4(), ev5.EvaluatorDeJong5()]
    eval_to_use = eval_list[int(config[0])]

    r_seed = int(config[1])
    run_count = int(config[2])
    
    ##########################################
    # Params needs to be array size 4
    # Population Size
    # Generation Count
    # Crossover Probability
    # Mutation Probability
    params = [int(config[3]), int(config[4]), config[5], config[6]]
    ##########################################

    for i in range(run_count):
        np.random.seed(r_seed + i)
        gen_algo = ga.GeneticAlgorithm(eval_to_use, params)
        if(config[7] == 1.0):
            gen_algo.run_chc()
        else:
            gen_algo.run_sga()

##########################################################################  

##########################################################################  
if __name__ == "__main__":
    main()
##########################################################################  