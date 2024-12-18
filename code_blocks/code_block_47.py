>>> def f():
...     return ['foo', 'bar', 'baz', 'qux']
...  

>>> f()
['foo', 'bar', 'baz', 'qux']
>>> f()[2]
'baz'
>>> f()[::-1]
['qux', 'baz', 'bar', 'foo']
