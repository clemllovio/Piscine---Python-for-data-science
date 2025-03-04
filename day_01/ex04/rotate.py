from load_image import ft_load
import numpy as np
import cv2

def ft_transpose(image: list):
    nbr_rows = len(image)
    nbr_cols = len(image[0])

    img_transposed = []

    for i in range(nbr_cols):
        row = []
        for j in range(nbr_rows):
            row.append(image[j][i])
        img_transposed.append(row)
    array = np.array(img_transposed)
    print(f"New shape after slicing: {array.shape}")
    return array

def ft_zoom(image: list):
    height, width = image.shape[:2]
    bigger = image[int(height * 0.25):int(height * 0.8), int(width * 0.4):int(width * 0.8)]

    print(f"New shape after slicing: {bigger.shape}")
    return bigger

def main():
    try:
        image = ft_load("animal.jpeg")
    except Exception as e:
        print(e)

    print(image)

    bigger = ft_zoom(image)

    img_tranposed = ft_transpose(bigger)
    cv2.imshow("img_tranposed", img_tranposed)
    cv2.waitKey(0)



if __name__ == "__main__":
    main()