from load_image import ft_load
import numpy as np
import cv2

def ft_invert(array) -> np.ndarray:
    img_invert = [[[255 - k for k in j] for j in i] for i in array]
    array = np.array(img_invert)
    return array

def ft_red(array) -> np.ndarray:
    red_component = array.copy()
    red_component[:, :, 1] = 0
    red_component[:, :, 0] = 0
    return red_component

def ft_green(array) -> np.ndarray:
    green_component = array.copy()
    green_component[::, ::, [0, 2]] = 0
    return green_component

def ft_blue(array) -> np.ndarray:
    blue_component = array.copy()
    blue_component[::, ::, 1:3] = 0
    return blue_component

# def ft_grey(array) -> np.ndarray:

def main():
    try:
        image = ft_load("landscape.jpg")
    except Exception as e:
        print(e)
        return

    print(image)

    bigger = ft_red(image)

    cv2.imshow("img_tranposed", bigger)
    cv2.waitKey(0)


if __name__ == "__main__":
    main()