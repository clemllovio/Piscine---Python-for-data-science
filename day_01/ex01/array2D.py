import numpy as np


def slice_me(family: list, start: int, end: int) -> list:
    """
    Slices a 2D list  between the given start and end indices.
    """
    if (type(family) is not list or type(start) is not int
            or type(end) is not int):
        raise TypeError

    array = np.array(family)
    print(f"My shape is : {array.shape}")

    new_array = array[start:end]
    print(f"My new shape is : {new_array.shape}")
    return new_array.tolist()
