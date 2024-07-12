from PIL import Image
import numpy as np


def display_and_save_image(array: np.ndarray, name: str):
    """
    Save the image witih the name given
    """
    if array is not None:
        output_file_name = name.replace(" ", "_")
        output_file_name += ".jpg"
        img = Image.fromarray(array)
        img.save(output_file_name)

    else:
        raise AssertionError("No image data to display.")


def ft_load(path: str) -> np.ndarray:
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

        return img_array

    except Exception as e:
        print(f"Error loading image: {e}")
        return None


if __name__ == "__main__":
    img = ft_load("./animal.jpeg")
    print(img)
