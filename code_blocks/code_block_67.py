>>> def avg(*args):
...     total = 0
...     for i in args:
...         total += i
...     return total / len(args)
...

>>> avg(1, 2, 3)
2.0
>>> avg(1, 2, 3, 4, 5)
3.0
