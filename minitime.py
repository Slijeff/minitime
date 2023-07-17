import time
from contextlib import contextmanager
from typing import Callable

def minitime(f: Callable):
    """Time a function, prints the time in nanosecond. Example: @minitime

    Args:
        f (Callable): The underlying function that decorator wraps
    """
    def time_func(*args, **kwargs):
        ts = time.perf_counter_ns()
        result = f(*args, **kwargs)
        te = time.perf_counter_ns()
        formatted = [a for a in args]
        formatted.extend([f'{k}={v}' for k, v in kwargs.items()])
        print(f'{f.__name__}({",".join(map(str, formatted))}) took {te - ts}ns')
        return result
    return time_func

@contextmanager
def minitime_context(name: str):
    """Time a block of code, prints the time in nanosecond. Example: with minitime_context("snippet_1")

    Args:
        name (str): the name of the code block
    """
    ts = time.perf_counter_ns()
    try:
        yield
    finally:
        print(f'Code[{name}] took {time.perf_counter_ns() - ts}ns')