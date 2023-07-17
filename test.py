from minitime import minitime, minitime_context


@minitime
@minitime
def f():
    pass

f()

with minitime_context("1"):
    with minitime_context("2"):
        pass