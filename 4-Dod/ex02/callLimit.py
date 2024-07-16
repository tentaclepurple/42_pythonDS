def callLimit(limit: int):
    count = 0

    def callLimiter(function):
        def limit_function(*args, **kwds):
            nonlocal count
            if count >= limit:
                print(f"Error: {function} call too many times")
                return
            count += 1
            return function(*args, **kwds)
        return limit_function

    return callLimiter


def main():

    @callLimit(3)
    def f():
        print("f()")
    f()
    f()
    f()
    f()


if __name__ == "__main__":
    main()
