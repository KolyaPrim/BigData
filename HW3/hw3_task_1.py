
def cache(times):
    def counter(func):
        def mind():
            mind.count += 1
            if mind.count == 1 or mind.count == times + 2:
                mind.x = func()
                mind.count = 1
            else:
                print(mind.x)

        mind.x = ''
        mind.count = 0
        return mind
    return counter

@cache(times=3)
def f():
    return input('? ')


f()
f()
f()
f()
f()
f()
f()
f()
f()
f()

