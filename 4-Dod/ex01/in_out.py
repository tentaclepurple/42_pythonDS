def square(x: int | float) -> int | float:
    """
    This function takes a number and returns
    the square of that number.
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    This function takes a number and returns
    the number raised to the power of itself.
    """
    return x ** x


def outer(x: int | float, func) -> object:
    """
    This function takes a number and a function
    as input and returns a function that takes no arguments.
    """
    if not isinstance(x, (int, float)):
        raise TypeError("x must be an int or a float")

    count = 0

    def inner() -> float:
        """
        calls the function passed to outer 'count' times
        """
        nonlocal count
        count += 1
        result = x
        for _ in range(count):
            result = func(result)
        return result

    return inner


def main():

    test = outer(45, square)
    print(test())
    print(test())
    print(test())


if __name__ == "__main__":
    main()
