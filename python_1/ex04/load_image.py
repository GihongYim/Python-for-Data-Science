import numpy as np
from PIL import Image


def ft_load(filename):
    img = Image.open(filename)
    return img


def main():
    ft_load("animal.jpeg")

if __name__ == "__main__":
    main()