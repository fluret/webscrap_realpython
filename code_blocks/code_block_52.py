 1procedure double(var x : integer);
 2begin
 3    x := x * 2;
 4end;
 5
 6var
 7    x : integer;
 8
 9begin
10    x := 5;
11    writeln('Before procedure call: ', x);
12    double(x);
13    writeln('After procedure call:  ', x);
14end.
