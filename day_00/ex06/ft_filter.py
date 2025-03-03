def ft_filter(function, iterable):
    return (item for item in iterable if function is None or function(item))

