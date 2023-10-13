from load_image import ft_load
import numpy as np
import matplotlib.pyplot as plt

def zoom():
    img = ft_load("animal.jpeg").convert('L')
    array = np.array(img)
    w, h = img.size
    zoom_size = 400
    zoom_img = img.crop((w / 2 - zoom_size / 2, h / 2 -zoom_size / 2, w / 2 + zoom_size / 2, h / 2 + zoom_size / 2))
    print(f'The shape of image is: {array.shape}')
    array = np.array(img)
    print(array)
    print('New shape after slicing: (400, 400, 1) or (400 ,400)')
    zoom_array = np.array(zoom_img)
    print(zoom_array)
    fsig = plt.figure()
    plt.imshow(zoom_array)
    plt.show()


def main():
    zoom()

if __name__ == '__main__':
    main()