import numpy as np
from PIL import Image


def ft_load(filename):
    """_summary_
        load image and print RGB value for each pixel
    Args:
        filename (_type_): valid for Image.open() function
    Return:
        None
    """

    img = Image.open(filename)
    x = np.array(img)
    print(f'The shape of image is: {x.shape}')
    print(x)


def main():
    ft_load("landscape.jpeg")


if __name__ == "__main__":
    main()