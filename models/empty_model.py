from models.proportion_model import ProportionModel
'''
Model for inferring whether the sequence of values is basically empty.
'''
class EmptyModel(ProportionModel):
    def __init__(self, default=None):
        ProportionModel.__init__(self)
        self.default = default

    def try_convert(self, value):
        try:
            # Remove quotes, newlines, and spaces.
            val_as_str = str(value).replace("'","").replace('"',"").replace("\n", "").strip()
            return val_as_str == "", None
        except:
            return False, None

    def default_value(self):
        return self.default

    def type_name(self):
        return "empty"
