from typeinfer import TypeInfer

'''
Ensure we can infer the type when everything is a number.
'''
def test_all_numbers():
    t = TypeInfer()
    for i in range(1000):
        t.add_value(i)
    assert t.infer_type() == "number"

'''
Ensure we can infer the type when everything is a string.
'''
def test_all_strings():
    t = TypeInfer()
    for i in range(1000):
        t.add_value("something")
    assert t.infer_type() == "string"

'''
Ensure we can infer the type when most of the values are numbers.
'''
def test_mostly_numbers():
    t = TypeInfer()
    for i in range(1000):
        t.add_value(i)
    for i in range(10):
        t.add_value("None")
    assert t.infer_type() == "number"
