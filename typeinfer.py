from models.number_model import NumberModel
from models.string_model import StringModel 

'''
Infer the type of a sequence of values.
'''
class TypeInfer:
    '''
    models_with_thresholds is used to configure this object.

    It should be a tuple of 2-element tuples. That is, it should take the form:

    ((model1, threshold1), (model2, threshold2), ..., (modelN, thresholdN))

    Each model (i.e. model1, model2, ..., modelN) should be of type InferenceModel.

    Each threshold (i.e. threshold1, threshold2, ..., thresholdN) should be a float between 0.0 and 1.0.

    After feeding this object a sequence of values, type inference works like this

    for i = 1 to N
        if model i has accuracy >= threshold i
            return model i's typename

    if none of the models have the desired accuracy, then the type inference returns None.

    If a models_with_thresholds is not specified, the default is:

    ((NumberModel, 0.9), (StringModel, 0.9))
    '''
    def __init__(self, models_with_thresholds=None):
        if models_with_thresholds is None:
            models_with_thresholds = ((NumberModel, 0.9), (StringModel, 0.9))
        self.models_with_thresholds = models_with_thresholds


    '''
    Add the given value to the model.
    '''
    def add_value(self, value):
        for model, threshold in self.models_with_thresholds:
            model.add_value(value)

    '''
    Returns the type_name of the inferred type. If you have not specified your own models_with_thresholds,
    this will be either "string" or "number", if the type inference was successful. If the type 
    inference failed, then None will be returned.
    '''
    def infer_type(self):
        for model, threshold in self.models_with_thresholds:
            if model.accuracy() >= threshold:
                return model.type_name()
        return None
