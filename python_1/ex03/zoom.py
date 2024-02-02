from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def zoom(filename: str, box: tuple) -> None:
    """
        Args:
            filename : str
        Returns:
            None
        load the image "${filename}.jpeg"
        print information about it
        diaplay it after zooming
    """
    array = ft_load(filename)
    r, g, b = array[:, :, 0], array[:, :, 1], array[:, :, 2]
    gray_array = 0.2989 * r + 0.5870 * g + 0.1140 * b
    gray_array = gray_array.astype('uint8')
    gray_img = Image.fromarray(gray_array)
    zoom_img = gray_img.crop(box)
    zoom_array = np.array(zoom_img)

    print(f'New shape after slicing: {zoom_array.shape}')
    print(zoom_array)
    plt.figure()
    plt.imshow(zoom_array, cmap='gray')
    plt.show()


def main():
    """main function"""
    left = 440
    up = 100
    zoom_size = 400
    right = left + zoom_size
    down = up + zoom_size
    zoom("animal.jpeg", (left, up, right, down))


if __name__ == '__main__':
    main()
