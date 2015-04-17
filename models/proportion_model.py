from models.inference_model import InferenceModel
'''
An inference model which infers types by trying to cast each value into a given type.
It counts the number of times the conversion is successful (and the total number of values).
The accuracy is the proportion of successful conversions.
'''
class ProportionModel(InferenceModel):
    def __init__(self):
        self.num_successes = 0.0
        self.num_trials = 0

    '''
    Subclasses of ProportionModel should override this method.

    It returns a tuple (conversion_successful, converted_value) where conversion_successful is a 
    boolean indicating whether the conversion succeeded. If conversion_successful == True, then
    converted_value is the result of the conversion.
    '''
    def try_convert(self, value):
        raise NotImplementedError("Subclass must implement try_convert")

    '''
    Subclasses of ProportionModel should override this method.

    It returns a sensible default value.
    '''
    def default_value(self):
        raise NotImplementedError("Subclass must implement default_value")

    '''
    Subclasses of ProportionModel should override this method.

    A string representation of the name of the type that the model is inferring.
    '''
    def type_name(self):
        raise NotImplementedError("Subclass must implement type_name")

    '''
    Return the result of converting value to the type that this inference model supports. If the
    value cannot be converted, use a sensible default.
    '''
    def convert(self, value):
        success, val = self.try_convert(value)
        if success:
            return val
        return self.default_value()

    '''
    Attempt to convert the value, and mark it as a success if conversion worked.
    '''
    def add_value(self, value):
        if self.can_convert(value):
            self.num_successes += 1
        self.num_trials += 1
    
    '''
    Return the proportion of successes. A model that has not been fed any values has an accuracy
    of 0.
    '''
    def accuracy(self):
        if self.num_trials == 0:
            return 0
        return self.num_successes / self.num_trials
