from PIL import Image


def ft_invert(array):
    """Inverts the color of the image received."""
    try:
        assert array.ndim == 3 and array.shape[2] == 3, \
            "image is not RGB image"
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        exit(1)

    inverted_array = array.copy()
    inverted_array = 255 - inverted_array
    image = Image.fromarray(inverted_array)
    image.show()
    return inverted_array


def ft_red(array):
    """Change the image to red."""
    try:
        assert array.ndim == 3 and array.shape[2] == 3, \
            "image is not RGB image"
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        exit(1)

    red_array = array.copy()
    red_array[:, :, 1] = 0
    red_array[:, :, 2] = 0
    image = Image.fromarray(red_array)
    image.show()
    return red_array


def ft_green(array):
    """Change the image to green."""
    try:
        assert array.ndim == 3 and array.shape[2] == 3, \
            "image is not RGB image"
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        exit(1)

    green_array = array.copy()
    green_array[:, :, 0] = 0
    green_array[:, :, 2] = 0
    image = Image.fromarray(green_array)
    image.show()
    return green_array


def ft_blue(array):
    """Change the image to blue."""
    try:
        assert array.ndim == 3 and array.shape[2] == 3, \
            "image is not RGB image"
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        exit(1)

    blue_array = array.copy()
    blue_array[:, :, 0] = 0
    blue_array[:, :, 1] = 0
    image = Image.fromarray(blue_array)
    image.show()
    return blue_array


def ft_grey(array):
    """Change the image to grey."""
    try:
        assert array.ndim == 3 and array.shape[2] == 3, \
            "image is not RGB image"
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        exit(1)
    
    grey_array = array.copy()
    gray_scale =\
        0.3 * grey_array[:, :, 0] +\
        0.59 * grey_array[:, :, 1] +\
        0.11 * grey_array[:, :, 2]
    grey_array[:, :, 0] = gray_scale
    grey_array[:, :, 1] = gray_scale
    grey_array[:, :, 2] = gray_scale
    image = Image.fromarray(grey_array)
    image.show()
    return grey_array
