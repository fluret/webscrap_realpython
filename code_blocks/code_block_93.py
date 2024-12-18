>>> def oper(x, y, *ignore, op='+'):
...     if op == '+':
...             return x + y
...     elif op == '-':
...             return x - y
...     elif op == '/':
...             return x / y
...     else:
...             return None
...

>>> oper(3, 4, op='+')
7
>>> oper(3, 4, op='/')
0.75
