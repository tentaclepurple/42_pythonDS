from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def display_and_save_image(array: np.ndarray, name: str):
    """
    Display the image with x and y axis labels and save the plot.
    """
    if array is not None:
        plt.imshow(array[:, :, 0], cmap='gray')
        plt.xlabel('X-axis')
        plt.ylabel('Y-axis')
        plt.title(str)
        output_file_name = name.replace(" ", "_")
        output_file_name += ".jpg"
        plt.savefig(output_file_name)
        plt.show()
    else:
        raise AssertionError("No image data to display.")


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
