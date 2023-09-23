import numpy as np

class Individual:

    ########################################################################## 
    # Without a chromosome parameter, the individual will be randomly generated.
    def __init__(self, chrom_len, chrom = None):

        self.chromosome = np.random.randint(0, 2, size=chrom_len) if chrom == None else chrom
        self.fitness = -1.0 # Unevaluated individuals will have fitness of -1 
    ########################################################################## 
