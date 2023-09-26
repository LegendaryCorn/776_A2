from eval import eval_base

class EvaluatorDeJong5(eval_base.Evaluator):
    ########################################################################## 
    def __init__(self):
        self.decode_keys = []
        self.decode_keys.append(eval_base.DecodeKey(-65.536, 65.535, 0.001))
        self.decode_keys.append(eval_base.DecodeKey(-65.536, 65.535, 0.001))
        self.a0 = [-32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32, -32, -16, 0, 16, 32]
        self.a1 = [-32, -32, -32, -32, -32, -16, -16, -16, -16, -16, 0, 0, 0, 0, 0, 16, 16, 16, 16, 16, 32, 32, 32, 32, 32]
    ##########################################################################
  
    ########################################################################## 
    # Maximum fitness should be around 1. Worse performers are closer to 0.
    def evaluate(self, params):

        obj = 0.002

        for i in range(25):
            obj += 1 / (i + 1 + pow(params[0] - self.a0[i], 6) + pow(params[1] - self.a1[i], 6))

        return obj
    ########################################################################## 