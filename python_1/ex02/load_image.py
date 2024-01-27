import numpy as np
from PIL import Image


def ft_load(path: str) -> np.array:
    """_summary_

    Args:
        path (str): image filepath

    Returns:
        np.array: image pixel array
    """
    try:
        img = Image.open(path)
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        exit()
    x = np.array(img)
    print(f"The shape of image is: {x.shape}")
    print(x)
    return x
