# typeinfer
Python library for inferring types of a sequence of values.

# Introduction
When parsing csv files, it's useful to determine the types of the columns. However, csv files don't provide this information, 
we have to infer it. This is challenging for a number of reasons, such as

1. **Missing values**: Some entries could be missing. We need to fill these in with a sensible default.
2. **Default values**: Some entries could have default values (ex. "N/A", "Unknown") which need to be tracked down and replaced with a sensible value.
3. **Multi-parseability**: Some entries could be parsed as multiple data types. For example, 123 could be a number `123` or a string `"123"`.

`typeinfer` is a library to infer types from a sequence of values intelligently.

# Intuition
To check if a sequence of values **has a given type**, look at each element and see if you can convert
it to that type. If the proportion of successful conversions is above a threshold (`typeinfer`
defaults to 90%), then assume that the sequence has the given type.

# Usage
## Basic
Create an object.

`t = TypeInfer()`

Feed it some values.

```
t.add_value("12,000")
t.add_value("54,232")
...
t.add_value("N/A")
t.add_value("1232")
```

Infer the type (it will be either `"empty"`, `"boolean"`, `"string"`, `"number"`, or `None`).

`inferred_type = t.infer_type()`

In the example above `inferred_type == "number"`.

## Row-at-a-time
Create an object.

`t = ManyTypeInfer()`

Feed it some rows (each row is a tuple and each must have the same number of elements).

```
t.add_value(("John", "Smith", "Yes", "12,000"))
t.add_value(("Jane", "Doe", "No", "30,000"))
t.add_value(("Alyssa", "Hacker", "Yes", "20,000"))
...
```

Infer the types of the columns.

`col_types = t.infer_column_types()`

In the example above, `col_types == ("string", "string", "boolean", "number")`

## Custom Type Inference
Create your own model `models/my_type_model.py` and extend the `ProportionModel` or `InferenceModel`
classes (see `models/proportion_model.py` and `models/inference_model.py`, respectively). 

Then, create your `TypeInfer` object with the models and threshold that you want.

`t = TypeInfer((MyModel(), 0.9), (StringModel(), 0.9))`
