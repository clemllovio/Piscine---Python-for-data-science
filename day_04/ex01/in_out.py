def square(x: int | float) -> int | float:
    """ Returns the square of the given number."""
    try:
        return x ** 2
    except TypeError as e:
        print(f"TypeError: {e}")


def pow(x: int | float) -> int | float:
    """Returns the result of raising the number to the power of itself."""
    try:
        return x ** x
    except TypeError as e:
        print(f"TypeError: {e}")


def outer(x: int | float, function) -> object:
    """Returns a function that applies the given `function`
    iteratively, starting with the value `x`"""
    count = 0

    def inner() -> float:
        """On the first call, it applies `function`
        to the initial value `x`.
        On subsequent calls, it applies `function`
        to the result of the previous call, returning the new result."""
        nonlocal count
        if count == 0:
            count = function(x)
        else:
            count = function(count)
        return count
    return inner
