from eval import eval_base
import numpy as np

class EvaluatorDeJong4(eval_base.Evaluator):
    ########################################################################## 
    def __init__(self):
        self.decode_keys = []
        for i in range(30):
            self.decode_keys.append(eval_base.DecodeKey(-1.28, 1.27, 0.01))
    ##########################################################################
  
    ########################################################################## 
    # Maximum fitness is weird because of the randomness. Above 0.1 means that the parameters are likely correct.
    def evaluate(self, params):

        obj = 0

        for i in range(len(params)):
            obj += (i+1) * pow(params[i], 4)
        obj += np.random.normal(0, 1) # Noise

        return 1.0 / (obj + 10.0)
    ########################################################################## 