>>> def f(a, b):
...     return
...

>>> f.__annotations__ = {'a': int, 'b': str, 'return': float}

>>> f.__annotations__
{'a': <class 'int'>, 'b': <class 'str'>, 'return': <class 'float'>}
