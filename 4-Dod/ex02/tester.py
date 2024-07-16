from callLimit import callLimit

@callLimit(3)
def f():
    print("f()")


f()
f()
f()
f()