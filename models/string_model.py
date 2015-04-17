'''
Model for inferring whether the sequence of values has a string type.
'''
class StringModel(ProportionModel):
    def __init__(self, default=""):
        self.default = default

    def try_convert(self, value):
        try:
            val = str(value)
            return True, val
        except:
            return False, None

    def default_value(self):
        return self.default

    def type_name(self):
        return "string"
