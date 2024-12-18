>>> def f() -> 0:
...     f.__annotations__['return'] += 1
...     print(f"f() has been executed {f.__annotations__['return']} time(s)")
...

>>> f()
f() has been executed 1 time(s)
>>> f()
f() has been executed 2 time(s)
>>> f()
f() has been executed 3 time(s)
