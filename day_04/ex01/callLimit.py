def callLimit(limit: int):
    """Returns a decorator that limits the number
    of times a function can be called."""
    count = 0

    def callLimiter(function):
        """ A decorator that limits the number of
        times the wrapped function can be called."""

        def limit_function(*args: any, **kwds: any,):
            """Executes the wrapped function if the call limit is not exceeded.
            Increments the call count each time the function is called."""
            nonlocal count
            if count >= limit:
                print(f"Error: {function} called too many times")
                return None
            count += 1
            return function()
        return limit_function
    return callLimiter
