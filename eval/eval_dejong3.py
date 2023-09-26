from eval import eval_base
import math

class EvaluatorDeJong3(eval_base.Evaluator):
    ########################################################################## 
    def __init__(self):
        self.decode_keys = []
        self.decode_keys.append(eval_base.DecodeKey(-5.12, 5.11, 0.01))
        self.decode_keys.append(eval_base.DecodeKey(-5.12, 5.11, 0.01))
        self.decode_keys.append(eval_base.DecodeKey(-5.12, 5.11, 0.01))
        self.decode_keys.append(eval_base.DecodeKey(-5.12, 5.11, 0.01))
        self.decode_keys.append(eval_base.DecodeKey(-5.12, 5.11, 0.01))
    ##########################################################################
  
    ########################################################################## 
    # Maximum fitness is 55 assuming there are 5 parameters. Minimum is always 0 when all numbers are greater than or equal to 5.
    def evaluate(self, params):

        obj = 0

        for param in params:
            obj += math.floor(param)

        return 5.0 * len(params) - obj
    ########################################################################## 