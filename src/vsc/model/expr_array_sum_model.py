'''
Created on Jun 27, 2020

@author: ballance
'''
from vsc.model.expr_dynamic_model import ExprDynamicModel

class ExprArraySumModel(ExprDynamicModel):
    
    def __init__(self, arr):
        super().__init__()
        self.arr = arr
        
    def is_signed(self):
        return self.arr.is_signed
    
    def width(self):
        ret = self.arr.width
        if ret < 32:
            ret = 32
        return ret
    
    def build_expr(self):
        return self.arr.get_sum_expr()
    
    def build(self, btor):
        return self.arr.build_sum_expr(btor)
    
    def accept(self, v):
        v.visit_expr_array_sum(self)
    