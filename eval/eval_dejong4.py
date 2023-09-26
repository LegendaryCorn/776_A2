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
    # Maximum fitness should be around 1. Worse performers are closer to 0.
    def evaluate(self, params):

        obj = 0

        for i in range(len(params)):
            obj += (i+1) * pow(params[i], 4)
            obj += np.random.normal(0, 1) # The random

        return 1.0 / (obj + 1.0) # Because of the noise, I have to change this a bit
    ########################################################################## 