from typeinfer import TypeInfer

'''
Ensure we can infer the type when everything is a number.
'''
def test_all_numbers():
    t = TypeInfer()
    for i in xrange(1000):
        t.add_value("%d" % (i,))
    assert t.infer_type() == "number"

'''
Ensure we can infer the type when everything is a string.
'''
def test_all_strings():
    t = TypeInfer()
    for i in xrange(1000):
        t.add_value("something")
    assert t.infer_type() == "string"

'''
Ensure we can infer the type when most of the values are numbers.
'''
def test_mostly_numbers():
    t = TypeInfer()
    for i in xrange(1000):
        t.add_value("%d" % (i,) )
    for i in xrange(10):
        t.add_value("None")
    assert t.infer_type() == "number"

'''
Ensure that we can infer a numeric type even when the numbers are messy
'''
def test_messy_numbers():
    t = TypeInfer()
    for i in xrange(100):
        t.add_value(" 102,000 ")
    for i in xrange(5):
        t.add_value("String")
    for i in xrange(5):
        t.add_value("yes")
    assert t.infer_type() == "number"

'''
Ensure that we can infer a boolean type
'''
def test_boolean():
    # First test with True/False.
    t = TypeInfer()
    for i in xrange(100):
        t.add_value(False)
    for i in xrange(20):
        t.add_value(True)
    assert t.infer_type() == "boolean"
    
    # Now test with 1/0.
    t = TypeInfer()
    for i in xrange(100):
        t.add_value(0)
    for i in xrange(20):
        t.add_value(1)
    assert t.infer_type() == "boolean"

    # Now test with YeS/nO.
    t = TypeInfer()
    for i in xrange(100):
        t.add_value("YeS")
    for i in xrange(20):
        t.add_value("nO")
    assert t.infer_type() == "boolean"

'''
Ensure that we can infer a boolean type even when there is other junk.
'''
def test_messy_boolean():
    t = TypeInfer()
    for i in xrange(100):
        t.add_value(False)
    for i in xrange(20):
        t.add_value(True)
    for i in xrange(10):
        t.add_value("102")
    for i in xrange(2):
        t.add_value("Nothing")
    assert t.infer_type() == "boolean"

'''
Ensure that we can infer an empty type.
'''
def test_empty():
    t = TypeInfer()
    for i in xrange(100):
        t.add_value('" "') # Make the values be empty quotes.
    assert t.infer_type() == "empty"

'''
Ensure that we don't infer the empty type if there is at least one non-empty value.
'''
def test_no_wrong_empty():
    t = TypeInfer()
    for i in xrange(1000):
        t.add_value("' '")
    t.add_value("Because of this, it's not empty anymore")
    assert t.infer_type() == "string"

