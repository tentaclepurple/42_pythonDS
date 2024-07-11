from PIL import Image
import numpy as np
from numpy import ndarray


def ft_load(path: str) -> ndarray:
    """
        Load image from path and return as numpy array
        options:
        format = img.format (JPEG, PNG, BMP, etc)
        mode = img.mode (RGB, RGBA, L, etc)
        size = img.size (width, height)
        print(f"Format: {format}, Mode: {mode}, Size: {size}")
    """
    try:

        img = Image.open(path)

        img_array = np.array(img)

        print(f"The shape of image is: {img_array.shape}")

        return img_array

    except Exception as e:
        print(f"Error loading image: {e}")
        return None


if __name__ == "__main__":
    img = ft_load("./animal.jpeg")
    print(img)
