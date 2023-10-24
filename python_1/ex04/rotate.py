from load_image import ft_load
import matplotlib.pyplot as plt
import numpy as np


def rotate():
    """
        rotate image animal.jpeg
    """
    img = ft_load("animal.jpeg").convert('L')
    w, h = img.size
    zoom_size = 400
    zoom_img = img.crop((
        w / 2 - zoom_size / 2,
        h / 2 - zoom_size / 2,
        w / 2 + zoom_size / 2,
        h / 2 + zoom_size / 2
        ))
    zoom_array = np.array(zoom_img)
    print(f'The shape of image is: ({zoom_size}, 400, 1) or (400, 400)')
    print(zoom_array)
    rotate_img = zoom_img.rotate(90)
    print('New shape after Transpose: (400 ,400)')
    rotate_array = np.array(rotate_img)
    print(rotate_array)
    plt.figure()
    plt.imshow(rotate_array, cmap="gray")
    plt.show()


def main():
    """
    main function
    """
    rotate()


if __name__ == "__main__":
    main()
