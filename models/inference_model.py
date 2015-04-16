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
        pass
    '''
    Return the inferred type (as a string) with a value num_passing.
    '''
    def infer_type(self):
        pass
    def convert(self, value):
        pass
