def ft_filter(function, iterable):
    """
    Custom implementation of the built-in filter() function.
    Filters elements from the given iterable based on the provided function.
    If the function is None, it returns all truthy elements from the iterable.
    """
    return (item for item in iterable if function is None or function(item))
