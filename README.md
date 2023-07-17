# Minitime
A tiny timing util that wraps around `time.perf_counter_ns()` under 40 LOC that can use to record functions and code snippet execution time.

## Examples
To time a function:
```
from minitime import minitime

@minitime
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

fib(4)

output:
fib(1) took 1200ns
fib(0) took 1700ns
fib(2) took 129700ns
fib(1) took 3000ns
fib(3) took 237800ns
fib(1) took 2000ns
fib(0) took 3600ns
fib(2) took 184200ns
fib(4) took 570300ns
```

To time arbitrary code snippets:
```
from minitime import minitime_context

with minitime_context("code_1"):
    2 ** 1000000

output:
Code[code_1] took 3865300ns
```
You can even time the time function itself:
```
@minitime
@minitime
def f():
    pass
f()
```
Or
```
with minitime_context("1"):
    with minitime_context("2"):
        pass
```