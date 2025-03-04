import cv2

def ft_load(path: str) -> list:
    image = cv2.imread(path)
    assert image is not None, "file could not be opened"
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    print(f"The shape of image is: {image.shape}")

    return image
