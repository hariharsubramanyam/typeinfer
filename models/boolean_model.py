from models.proportion_model import ProportionModel
'''
Model for inferring whether the sequence of values has a boolean type.
'''
class BooleanModel(ProportionModel):
    def __init__(self, default=False):
        ProportionModel.__init__(self)
        self.default = default

    def try_convert(self, value):
        try:
            lower_str_val = str(value).lower()
            if lower_str_val in ["1", "yes", "y", "true", "+"]:
                return True, True
            elif lower_str_val in ["0", "no", "n", "false", "-"]:
                return True, False

            return False, None 
        except:
            return False, None

    def default_value(self):
        return self.default

    def type_name(self):
        return "boolean"
