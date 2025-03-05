from load_image import ft_load
import numpy as np
import cv2


def ft_zoom(image: np.ndarray) -> np.ndarray:
    """
        Crops a central portion of the given image to create a zoom effect.
    """
    height, width = image.shape[:2]

    top, bottom = int(height * 0.2), int(height * 0.8)
    left, right = int(width * 0.3), int(width * 0.8)

    if bottom - top <= 0 or right - left <= 0:
        raise ValueError("Image is too small for the zoom operation.")

    zoomed_image = image[top:bottom, left:right]
    print(f"New shape after slicing: {zoomed_image.shape}")
    return zoomed_image


def main():
    """
        Loads an image, applies a zoom effect, and displays the result.
    """
    try:
        image = ft_load("animal.jpeg")
        print(image)
        zoomed_image = ft_zoom(image)
        print(zoomed_image)

        cv2.imshow("zoom_on_me", zoomed_image)
        while cv2.getWindowProperty('zoom_on_me', cv2.WND_PROP_VISIBLE) >= 1:
            keyCode = cv2.waitKey(1000)
            if keyCode == 27:
                break
        cv2.destroyAllWindows()
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except ValueError as e:
        print(f"Zoom Error: {e}")


if __name__ == "__main__":
    main()
