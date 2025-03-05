import numpy as np
import cv2


def ft_invert(array) -> np.ndarray:
    """
    Invert the colors of an image.
    """
    img_invert = [[[255 - k for k in j] for j in i] for i in array]
    inverted_image = np.array(img_invert)

    cv2.imshow("inverted_image", inverted_image)
    while cv2.getWindowProperty('inverted_image', cv2.WND_PROP_VISIBLE) >= 1:
        keyCode = cv2.waitKey(1000)
        if keyCode == 27:
            break
    cv2.destroyAllWindows()

    return inverted_image


def ft_red(array) -> np.ndarray:
    """
    Set the green and blue components of an image to 0.
    """
    red_image = array.copy()
    red_image[:, :, 1] = 0
    red_image[:, :, 0] = 0

    cv2.imshow("red_image", red_image)
    while cv2.getWindowProperty('red_image', cv2.WND_PROP_VISIBLE) >= 1:
        keyCode = cv2.waitKey(1000)
        if keyCode == 27:
            break
    cv2.destroyAllWindows()

    return red_image


def ft_green(array) -> np.ndarray:
    """
    Set the red and blue components of an image to 0.
    """
    green_image = array.copy()
    green_image[::, ::, [0, 2]] = 0

    cv2.imshow("green_image", green_image)
    while cv2.getWindowProperty('green_image', cv2.WND_PROP_VISIBLE) >= 1:
        keyCode = cv2.waitKey(1000)
        if keyCode == 27:
            break
    cv2.destroyAllWindows()
    return green_image


def ft_blue(array) -> np.ndarray:
    """
    Set the red and green components of an image to 0.
    """
    blue_image = array.copy()
    blue_image[::, ::, 1:3] = 0

    cv2.imshow("blue_image", blue_image)
    while cv2.getWindowProperty('blue_image', cv2.WND_PROP_VISIBLE) >= 1:
        keyCode = cv2.waitKey(1000)
        if keyCode == 27:
            break
    cv2.destroyAllWindows()

    return blue_image


def ft_grey(array) -> np.ndarray:
    """
    Converts a color image to grayscale using the standard luminosity formula.
    """
    grey_image = array.copy()
    height, width = grey_image.shape[:2]

    for i in range(height):
        for j in range(width):
            grey_image[i][j] = int(grey_image[i][j][0] * 0.2126
                                   + grey_image[i][j][1] * 0.7152 +
                                   grey_image[i][j][2] * 0.0722)

    cv2.imshow("grey_image", grey_image)
    while cv2.getWindowProperty('grey_image', cv2.WND_PROP_VISIBLE) >= 1:
        keyCode = cv2.waitKey(1000)
        if keyCode == 27:
            break
    cv2.destroyAllWindows()

    return grey_image
