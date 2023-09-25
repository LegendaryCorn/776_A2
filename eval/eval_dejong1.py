from eval import eval_base

class EvaluatorDeJong1(eval_base.Evaluator):
    ########################################################################## 
    def __init__(self):
        self.decode_keys = []
        self.decode_keys.append(eval_base.DecodeKey(-5.12, 5.11, 0.01))
        self.decode_keys.append(eval_base.DecodeKey(-5.12, 5.11, 0.01))
        self.decode_keys.append(eval_base.DecodeKey(-5.12, 5.11, 0.01))
    ##########################################################################
  
    ########################################################################## 
    # Maximum fitness is 1. Worse performers are closer to 0.
    def evaluate(self, params):

        obj = 0

        for param in params:
            obj += param * param

        return 1.0 / (obj + 1.0)
    ########################################################################## 