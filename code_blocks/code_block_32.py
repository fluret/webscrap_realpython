 1// Pascal Example #2
 2
 3procedure f(var fx : integer);
 4begin
 5    writeln('Start  f():  fx = ', fx);
 6    fx := 10;
 7    writeln('End    f():  fx = ', fx);
 8end;
 9
10// Main program
11var
12    x : integer;
13
14begin
15    x := 5;
16    writeln('Before f():  x = ', x);
17    f(x);
18    writeln('After  f():  x = ', x);
19end.
