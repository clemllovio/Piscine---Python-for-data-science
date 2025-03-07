def ft_statistics(*args: any, **kwargs: any) -> None:
    """Display the results of calcul depending on the kwargs"""
    len_args = len(args)
    for value in kwargs.values():
        if len_args == 0:
            print("ERROR")
        else:
            match value:
                case "mean":
                    mean_calcul(*args, length=len_args)
                case "median":
                    median_calcul(*args, length=len_args)
                case "quartile":
                    quartile_calcul(*args, length=len_args)
                case "std":
                    std_calcul(*args, length=len_args)
                case "var":
                    var_calcul(*args, length=len_args)


def mean_calcul(*args: any, length: int) -> None:
    """Calculate and print the mean (average) of the provided numbers"""
    try:
        print(f'mean : {sum(args) / length}')
    except TypeError as e:
        print(f'TypeError: {e}')


def median_calcul(*args: any, length: int) -> None:
    """Calculate and print the median of the provided numbers"""
    try:
        list_args = list(args)
        list_args.sort()

        if length % 2 == 0:
            median = ((list_args[length // 2]) +
                      (list_args[length // 2 + 1])) / 2
        else:
            median = list_args[length // 2]
        print(f'median : {median}')
    except TypeError as e:
        print(f'TypeError: {e}')


def quartile_calcul(*args: any, length: int) -> None:
    """Calculate and print the first (Q1) and third (Q3)
    quartiles of the provided numbers"""
    try:
        list_args = list(args)
        list_args.sort()

        q1_index = length // 4
        q3_index = (length * 3) // 4

        print(f'quartile : [{list_args[q1_index]}, {list_args[q3_index]}]')
    except TypeError as e:
        print(f'TypeError: {e}')


def std_calcul(*args: any, length: int) -> None:
    """Calculate and print the standard deviation of the provided numbers"""
    try:
        mean = sum(args) / length
        squared_diff = [(value - mean) ** 2 for value in args]
        variance = sum(squared_diff) / (length - 1 if length > 1 else length)

        std_dev = variance ** 0.5
        print(f'std : {std_dev}')
    except TypeError as e:
        print(f'TypeError: {e}')


def var_calcul(*args: any, length: int) -> None:
    """Calculate and print the variance of the provided numbers"""
    try:
        mean = sum(args) / length
        squared_diff = [(value - mean) ** 2 for value in args]
        variance = sum(squared_diff) / (length - 1 if length > 1 else length)

        print(f'var : {variance}')
    except TypeError as e:
        print(f'TypeError: {e}')
