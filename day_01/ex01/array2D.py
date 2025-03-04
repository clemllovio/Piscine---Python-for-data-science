import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    if type(family) != list or type(start) != int or type(end) != int:
        raise TypeError

    array = np.array(family)
    print(f"My shape is : {array.shape}")

    new_array = array[start:end]
    print(f"My new shape is : {new_array.shape}")
    return new_array