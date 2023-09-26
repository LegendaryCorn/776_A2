from eval import eval_base

class EvaluatorDeJong2(eval_base.Evaluator):
    ########################################################################## 
    def __init__(self):
        self.decode_keys = []
        self.decode_keys.append(eval_base.DecodeKey(-2.048, 2.047, 0.001))
        self.decode_keys.append(eval_base.DecodeKey(-2.048, 2.047, 0.001))
    ##########################################################################
  
    ########################################################################## 
    # Maximum fitness is 1. Worse performers are closer to 0.
    def evaluate(self, params):

        obj = 0
        
        for i in range(len(params) - 1):
            obj += 100 * (params[i+1] - params[i] * params[i]) * (params[i+1] - params[i] * params[i]) # First part
            obj += (params[i] - 1) *  (params[i] - 1) # Second part

        return 1.0 / (obj + 1.0)
    ########################################################################## 