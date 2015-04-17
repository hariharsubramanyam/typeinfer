from models.proportion_model import ProportionModel
'''
Model for inferring whether the sequence of values has a numeric type.
'''
class NumberModel(ProportionModel):
    def __init__(self, default=0):
        self.default = default

    def try_convert(self, value):
        try:
            value = str(value).replace(",", "") #TODO: For i18n, some countries use "," instead of ".". Handle that case.
            val = float(value)
            return True, val
        except:
            return False, None 
        
    def default_value(self):
        return self.default

    def type_name(self):
        return "number"
