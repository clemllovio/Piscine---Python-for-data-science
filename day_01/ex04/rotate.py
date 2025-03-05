from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


def ft_transpose(image: list) -> np.ndarray:
    """
    Transpose the given image.
    """
    nbr_rows = len(image)
    nbr_cols = len(image[0])

    transposed_image = []

    for i in range(nbr_cols):
        row = []
        for j in range(nbr_rows):
            row.append(image[j][i])
        transposed_image.append(row)
    array_image = np.array(transposed_image)
    print(f"New shape after Transpose: {array_image.shape}")
    return array_image


def ft_zoom(image: list) -> np.ndarray:
    """
        Crops a central portion of the given image to create a zoom effect.
    """
    height, width = image.shape[:2]

    top, bottom = int(height * 0.2), int(height * 0.8)
    left, right = int(width * 0.3), int(width * 0.8)

    if bottom - top <= 0 or right - left <= 0:
        raise ValueError("Image is too small for the zoom operation.")

    zoomed_image = image[top:bottom, left:right]
    return zoomed_image


def main():
    """
        Loads an image, applies a zoom effect, and displays the result.
    """
    try:
        image = ft_load("animal.jpeg")
        print(image)
        zoomed_image = ft_zoom(image)
        transposed_image = ft_transpose(zoomed_image)
        print(transposed_image)

        plt.imshow(transposed_image)
        plt.show()
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Zoom Error: {e}")


if __name__ == "__main__":
    main()
