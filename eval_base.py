import numpy as np

# This class will be used to convert a chromosome substring into a float that will be used in an evaluator.
# The evaluator MUST define this value.

class DecodeKey:
    ########################################################################## 
    def __init__(self, min, max, prec):
        self.min = min
        self.max = max
        self.bits = int(np.floor(np.log2(((max - min) / prec) + 1)))
        self.precision = (max - min) / (np.exp2(self.bits) - 1)
    ##########################################################################

    ##########################################################################
    # Converts a chromosome substring into a value
    def decode(self, chrom):
        chrom_val = 0.0
        e = 0
        for gene in chrom:
            chrom_val += pow(2, e) if gene == 1 else 0
            e += 1

        return chrom_val * self.precision + self.min
    ##########################################################################     


# This is a base class; other classes should inherit from it.
# This will make it easy to implement multiple evaluators.

class Evaluator:
    
    ########################################################################## 
    def __init__(self):
        self.decode_keys = []
    ########################################################################## 

    ########################################################################## 
    # Gets the chromosome length, assumes decode keys has a value.
    def get_chrom_len(self):

        total = 0

        for dkey in self.decode_keys:
            total += dkey.bits

        return total
    ##########################################################################    

    ########################################################################## 
    # Should not be changed in inherited classes.
    # This uses the keys of the class in order to convert a chromosome to parameters, and then convert those parameters to a fitness.
    def get_fitness(self, chrom):
        params = []
        i = 0

        # Convert chromosome to parameters
        for key in self.decode_keys:
            sub_chrom = chrom[i:i+key.bits]
            params.append(key.decode(sub_chrom))
            i += key.bits

        # Evaluate the parameters
        return self.evaluate(params)
    ########################################################################## 

    ########################################################################## 
    # This should ALWAYS return fitness. Never return the original objective value if it doesn't meet fitness criteria.
    def evaluate(self, params):
        return 1.0
    ########################################################################## 