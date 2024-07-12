from load_image import ft_load
import numpy as np


def ft_zoom(path: str, left, upper, right, lower) -> None:
    """
        Zoom image by cropping it
    """
    img, shape = ft_load(path)

    try:

        if lower > shape[0] or right > shape[1] or \
                left == right or upper == lower:
            raise AssertionError("Invalid zooming parameters")

        croped_img = img.crop((left, upper, right, lower))

        bn_img = croped_img.convert("L")

        arr = np.array(bn_img)

        if arr.ndim == 2:
            arr = np.expand_dims(arr, axis=2)

        """bn_img.save("zoomed_image.jpg") save image to disk"""

        print(f"New shape after slicing: {arr.shape}")
        print(arr)

        return arr

    except Exception as e:
        print(f"Error zooming image: {e}")


def main():
    left = 462
    upper = 100
    right = 862
    lower = 500
    ft_zoom("./animal.jpeg", left, upper, right, lower)


if __name__ == "__main__":
    main()
