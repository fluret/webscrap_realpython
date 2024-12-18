>>> def f(x):
...     x['bar'] = 22
...

>>> my_dict = {'foo': 1, 'bar': 2, 'baz': 3}

>>> f(my_dict)
>>> my_dict
{'foo': 1, 'bar': 22, 'baz': 3}
