>>> def f(a: int, b: str, c: float):
...     import inspect
...     args = inspect.getfullargspec(f).args
...     annotations = inspect.getfullargspec(f).annotations
...     for x in args:
...         print(x, '->',
...               'arg is', type(locals()[x]), ',',
...               'annotation is', annotations[x],
...               '/', (type(locals()[x])) is annotations[x])
...

>>> f(1, 'foo', 3.3)
a -> arg is <class 'int'> , annotation is <class 'int'> / True
b -> arg is <class 'str'> , annotation is <class 'str'> / True
c -> arg is <class 'float'> , annotation is <class 'float'> / True

>>> f('foo', 4.3, 9)
a -> arg is <class 'str'> , annotation is <class 'int'> / False
b -> arg is <class 'float'> , annotation is <class 'str'> / False
c -> arg is <class 'int'> , annotation is <class 'float'> / False

>>> f(1, 'foo', 'bar')
a -> arg is <class 'int'> , annotation is <class 'int'> / True
b -> arg is <class 'str'> , annotation is <class 'str'> / True
c -> arg is <class 'str'> , annotation is <class 'float'> / False
