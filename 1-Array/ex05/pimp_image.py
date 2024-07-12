from load_image import ft_load, display_and_save_image
import numpy as np


def ft_invert(arr: np.ndarray) -> np.ndarray:
    """
        Invert the image color
    """
    return 255 - arr


def ft_red(arr: np.ndarray) -> np.ndarray:
    """
        Set the red channel to 0
    """
    arr[:, :, 1] = 0    # green channel
    arr[:, :, 2] = 0    # blue channel

    return arr


def ft_green(arr: np.ndarray) -> np.ndarray:
    """
        Set the green channel to 0
    """
    arr[:, :, 0] = 0    # red channel
    arr[:, :, 2] = 0    # blue channel

    return arr


def ft_blue(arr: np.ndarray) -> np.ndarray:
    """
        Set the blue channel to 0
    """
    arr[:, :, 0] = 0    # red channel
    arr[:, :, 1] = 0    # green channel

    return arr


def grey_scale(arr: np.ndarray) -> np.ndarray:
    """
        Convert the image to grey scale
    """
    red_channel = arr[:, :, 0] / 3
    green_channel = arr[:, :, 1] / 3
    blue_channel = arr[:, :, 2] / 3
    grey_channel = red_channel + green_channel + blue_channel
    grey_channel = grey_channel.astype(np.uint8)

    grey_channel = grey_channel.astype(np.uint8)
    grey_image = np.stack([grey_channel, grey_channel, grey_channel], axis=2)

    print(grey_image.shape)
    return grey_image


def main():
    img = ft_load("./landscape.jpg")

    inverted = ft_invert(img.copy())
    display_and_save_image(inverted, "_inverted image")

    red = ft_red(img.copy())
    display_and_save_image(red, "_red filter image")

    green = ft_green(img.copy())
    display_and_save_image(green, "_green filter image")

    blue = ft_blue(img.copy())
    display_and_save_image(blue, "_blue filter image")

    grey = grey_scale(img.copy())
    display_and_save_image(grey, "_grey image")


if __name__ == "__main__":
    main()
