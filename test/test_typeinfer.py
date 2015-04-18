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
    for i in range(100):
        t.add_value(" 102,000 ")
    for i in range(5):
        t.add_value("String")
    assert t.infer_type() == "number"

