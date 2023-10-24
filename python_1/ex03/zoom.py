from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def zoom():
    """
        Args:
            None
        Returns:
            None
        load the image "animal.jpeg"
        print information about it
        diaplay it after zooming
    """
    array = ft_load("animal.jpeg")
    r, g, b = array[:, :, 0], array[:, :, 1], array[:, :, 2]
    gray_array = 0.2989 * r + 0.5870 * g + 0.1140 * b
    gray_array = gray_array.astype('uint8')
    gray_img = Image.fromarray(gray_array)
    w, h = gray_array.shape
    zoom_size = 400
    zoom_img = gray_img.crop(
        (w / 2 - zoom_size / 2,
         h / 2 - zoom_size / 2,
         w / 2 + zoom_size / 2,
         h / 2 + zoom_size / 2
         ))
    zoom_array = np.array(zoom_img)
    print(f'The shape of image is: {zoom_array.shape}')
    print(zoom_array)

    print('New shape after slicing: (400, 400, 1) or (400 ,400)')
    print(zoom_array)
    plt.figure()
    plt.imshow(zoom_array, cmap='gray')
    plt.show()


def main():
    """main function"""
    zoom()


if __name__ == '__main__':
    main()
