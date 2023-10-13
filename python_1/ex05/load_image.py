import numpy as np
from PIL import Image


def ft_load(filename):
    img = Image.open(filename)
    x = np.array(img)
    print(f'The shape of image is: {x.shape}')
    print(x)
    img.show()
    return x

def main():
    ft_load("animal.jpeg")

if __name__ == "__main__":
    main()