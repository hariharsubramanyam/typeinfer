'''
This is the class which forms the basis for classes with the type inference logic.

They should all extend this class and implement the methods listed.
'''
class InferenceModel:
    '''
    Add the given value to the inference model. The model should use this value to update its
    hypothesis about the type.
    '''
    def add_value(self, value):
        raise NotImplementedError("Subclass must implement add_value")
    '''
    Return a number between 0.0 and 1.0 indicating how likely the given values are of this type.
    The programmer can interpret the term "accuracy" as desired.
    '''
    def accuracy(self):
        raise NotImplementedError("Subclass must implement accuracy")

    '''
    Return the result of converting value to the type that this inference model supports. If the
    value cannot be converted, use a sensible default.
    '''
    def convert(self, value):
        raise NotImplementedError("Subclass must implement convert")

    '''
    A string representation of the name of the type that the model is inferring.
    '''
    def type_name(self):
        raise NotImplementedError("Subclass must implement type_name")
