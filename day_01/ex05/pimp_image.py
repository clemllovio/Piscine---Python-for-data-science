from load_image import ft_load
import numpy as np
import cv2


def ft_invert(array) -> np.ndarray:
    """
    Invert the colors of an image.
    """
    img_invert = [[[255 - k for k in j] for j in i] for i in array]
    array = np.array(img_invert)
    return array


def ft_red(array) -> np.ndarray:
    """
    Set the green and blue components of an image to 0.
    """
    red_component = array.copy()
    red_component[:, :, 1] = 0
    red_component[:, :, 0] = 0
    return red_component


def ft_green(array) -> np.ndarray:
    """
    Set the red and blue components of an image to 0.
    """
    green_component = array.copy()
    green_component[::, ::, [0, 2]] = 0
    return green_component


def ft_blue(array) -> np.ndarray:
    """
    Set the red and green components of an image to 0.
    """
    blue_component = array.copy()
    blue_component[::, ::, 1:3] = 0
    return blue_component


# def ft_grey(array) -> np.ndarray:

def main():
    try:
        image = ft_load("landscape.jpg")
        print(image)

        inv = ft_invert(image)
        red_image = ft_red(image)
        green_image = ft_green(image)
        blue_image = ft_blue(image)

        images = [image, inv, red_image, green_image, blue_image]

        current_index = 0

        while True:
            cv2.imshow("Image Viewer", images[current_index])

            key = cv2.waitKey(0)

            if key == 27:
                break
            elif key == 81:
                current_index = (current_index - 1) % len(images)
            elif key == 83:
                current_index = (current_index + 1) % len(images)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except FileNotFoundError as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
