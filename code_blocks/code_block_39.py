>>> def f(x):
...     x[0] = '---'
...

>>> my_list = ['foo', 'bar', 'baz', 'qux']

>>> f(my_list)
>>> my_list
['---', 'bar', 'baz', 'qux']
