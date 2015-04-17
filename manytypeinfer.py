from typeinfer import TypeInfer

'''
Perform type inference on rows at a time and return the
inferred type of each column.
'''
class ManyTypeInfer:
    def __init__(self):
        self.num_elements_in_row = None
        self.typeinfers = None

    '''
    Feed an entire row (i.e. a tuple of values) to the model.

    EVERY TIME YOU CALL THIS METHOD, YOU MUST CALL IT WITH THE SAME NUMBER OF ELEMENTS IN THE ROW.
    Otherwise, an exception will be thrown.
    '''
    def add_row(self, row):
        len_row = len(row)
        if self.num_elements_in_row is None:
            self.num_elements_in_row = len_row
            self.typeinfers = [TypeInfer() for i in xrange(self.num_elements_in_row)]
        if len_row != self.num_elements_in_row:
            raise Exception("add_row called initially with %d elements per row, but now called with %d elements per row" 
                    % (self.num_elements_in_row, len_row))
        for i in xrange(len_row):
            self.typeinfers[i].add_value(row[i])

    '''
    Returns a list of the type_names of the inferred type for each column.
    See the infer_type function in TypeInfer for more information. 
    '''
    def infer_column_types(self):
        return [t.infer_type() for t in self.typeinfers]


