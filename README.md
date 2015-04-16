# typeinfer
Python library for inferring types of a sequence of values.

# Introduction
When parsing csv files, it's useful to determine the types of the columns. However, csv files don't provide this information, 
we have to infer it. This is challenging for a number of reasons, such as

1. **Missing values**: Some entries could be missing. We need to fill these in with a sensible default.
2. **Default values**: Some entries could have default values (ex. "N/A", "Unknown") which need to be tracked down and replaced with a sensible value.
3. **Multi-parseability**: Some entries could be parsed as multiple data types. For example, 123 could be a number `123` or a string `"123"`.

`typeinfer` is a library to infer types from a sequence of values intelligently.
