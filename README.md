# 776_A2
 
To run this program, do 
> python.exe main.py config.txt

The math, matplotlib.pyplot, and numpy packages are needed to run the program.

The config file has several lines that can be adjusted:
DEJONG - Which of the 5 DeJong functions to use (integer between 1 and 5 inclusive)
SEEDSTART - A seed to start at (positive integer)
RUNS - Number of seeds to run this on (positive integer)
POPSIZE - Population size (positive integer divisible by 2)
GENCOUNT - Generation count (positive integer)
PCROSS - Probability of crossover (float between 0 and 1)
PMUT - Probability of mutation (float between 0 and 1)
USECHC - Whether to use CHC (1 if CHC, 0 if SGA)