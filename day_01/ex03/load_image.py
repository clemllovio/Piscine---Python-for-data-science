import cv2
import numpy as np


def ft_load(path: str) -> np.ndarray:
    """
    Load an image from a file and return it as a list.
    """
    image = cv2.imread(path)
    if image is None:
        raise FileNotFoundError(f"File '{path}' could not be opened.")
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    print(f"The shape of image is: {image.shape}")

    return image
