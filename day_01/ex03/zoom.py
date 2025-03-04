from load_image import ft_load
import cv2

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

    cv2.imshow("bigger", bigger)
    cv2.waitKey(0)



if __name__ == "__main__":
    main()