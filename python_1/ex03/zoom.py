from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt


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
    img = ft_load("animal.jpeg")
    array = np.array(img)
    print(f'The shape of image is: {array.shape}')
    print(array)
    gray_img = img.convert('L')
    gray_array = np.array(gray_img)
    w, h = gray_array.shape
    zoom_size = 400
    zoom_img = gray_img.crop(
        (w / 2 - zoom_size / 2,
         h / 2 - zoom_size / 2,
         w / 2 + zoom_size / 2,
         h / 2 + zoom_size / 2)
    )
    print('New shape after slicing: (400, 400, 1) or (400 ,400)')
    zoom_array = np.array(zoom_img)
    print(zoom_array)
    plt.figure()
    plt.imshow(zoom_array, cmap='gray')
    plt.show()


def main():
    """main function"""
    zoom()


if __name__ == '__main__':
    main()
