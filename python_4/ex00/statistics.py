def ft_statistics(*args: any, **kwargs: any) -> None:
    """
        ft_statistics function args: numbers,\
            kwargs {key:value} key: name value:statistical function
    """
    functions = {
        "mean": mean,
        "median": median,
        "quartile": quartile,
        "std": std,
        "var": var
        }
    for function in kwargs.values():
        if len(args) == 0:
            print("ERROR")
            continue
        if function in functions:
            print(f"{function} : {functions[function](args)}")
    return None


def mean(elements: tuple) -> float:
    """
    mean(elements : tuple) -> float

    Args:
        elements (tuple): tuple of numbers

    Returns:
        float: mean of elements (tuple)
    """
    elements_mean = sum(elements) / len(elements)
    return elements_mean


def median(elements: tuple) -> any:
    """median(elements: tuple) -> any

    Args:
        elements (tuple): _description_

    Returns:
        any: number : float or int
    """
    sorted_elements = sorted(elements)
    median_value = sorted_elements[len(elements) // 2]
    return median_value

def quartile(elements: tuple) -> any:
    """quartile(elements: tuple) -> any

    Args:
        elements (tuple): tuple of numbers

    Returns:
        any: quartile of elements
    """
    sorted_elements = sorted(elements)
    quartile_values = [
        sorted_elements[len(elements) // 4], sorted_elements[len(elements) * 3 // 4]]
    quartile_values = list(map(float, quartile_values))
    return quartile_values

def std(elements: tuple) -> float:
    """ std(elements: tuple) -> float

    Args:
        elements (tuple): tuple of numbers

    Returns:
        float: std of elements
    """
    elements_mean = mean(elements)
    deviation = list(map(lambda x: x - elements_mean, elements))
    variance = sum(list(map(lambda x: x ** 2, deviation))) / len(deviation)
    return variance ** (0.5)

def var(elements: tuple) -> float:
    """var(elements: tuple) -> float

    Args:
        elements (tuple): tuple of numbers

    Returns:
        float: variance of elements
    """
    elements_mean = mean(elements)
    deviation = list(map(lambda x: x - elements_mean, elements))
    variance = sum(list(map(lambda x: x ** 2, deviation))) / len(deviation)
    return variance


def main():
    pass


if __name__ == "__main__":
    main()
