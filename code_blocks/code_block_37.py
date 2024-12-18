 1>>> def f(fx):
 2...     print('fx =', fx, '/ id(fx) = ', id(fx))
 3...     fx = 10
 4...     print('fx =', fx, '/ id(fx) = ', id(fx))
 5...
 6
 7>>> x = 5
 8>>> print('x =', x, '/ id(x) = ', id(x))
 9x = 5 / id(x) =  1357924048
10
11>>> f(x)
12fx = 5 / id(fx) =  1357924048
13fx = 10 / id(fx) =  1357924128
14
15>>> print('x =', x, '/ id(x) = ', id(x))
16x = 5 / id(x) =  1357924048
