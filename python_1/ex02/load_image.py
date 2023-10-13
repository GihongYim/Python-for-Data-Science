import numpy as np
from PIL import Image


def ft_load(filename):
    img = Image.open(filename)
    x = np.array(img)
    print(f'The shape of image is: {x.shape}')
    print(x)


def main():
    ft_load("landscape.jpg")

if __name__ == "__main__":
    main()