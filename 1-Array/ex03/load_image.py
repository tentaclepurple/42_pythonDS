from PIL import Image
import numpy as np


def ft_load(path: str) -> tuple[Image.Image, tuple[int, int, int]]:
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

        if img_array.ndim != 3:
            raise AssertionError("Invalid image data")

        shape = img_array.shape

        print(f"The shape of image is: {shape}")
        print(img_array)

        return img, shape

    except Exception as e:
        print(f"Error loading image: {e}")
        return None


if __name__ == "__main__":
    img = ft_load("./animal.jpeg")
    print(img)
