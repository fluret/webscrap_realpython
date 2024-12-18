>>> def f(a: int = 12, b: str = 'baz') -> float:
...     print(a, b)
...     return(3.5)
...

>>> f.__annotations__
{'a': <class 'int'>, 'b': <class 'str'>, 'return': <class 'float'>}

>>> f()
12 baz
3.5
