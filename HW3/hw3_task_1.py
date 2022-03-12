from linecache import cache


# @cache(times=3)
def f():
    return input('? 1')  # careful with input() in python2, use raw_input() instead


f()