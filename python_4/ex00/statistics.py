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
    try:
        assert all(isinstance(arg, int | float) for arg in args), \
            "non-numerical value exist"
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        exit(1)
    for function in kwargs.values():
        try:
            assert len(args) > 0, "ERROR"
            if function in functions:
                print(f"{function} : {functions[function](args)}")
        except Exception as e:
            print(e)
    return None


def mean(elements: tuple) -> float | int:
    """
    mean(elements : tuple) -> float

    Args:
        elements (tuple): tuple of numbers

    Returns:
        float | int: mean of elements (tuple)
    """
    elements_mean = sum(elements) / len(elements)
    return elements_mean


def median(elements: tuple) -> float | int:
    """median(elements: tuple) -> any

    Args:
        elements (tuple): _description_

    Returns:
        float | int: median value
    """
    sorted_elements = sorted(elements)
    if len(sorted_elements) % 2 != 0:
        median_value = sorted_elements[len(elements) // 2]
    else:
        median_value = (sorted_elements[len(elements) // 2]
                        + sorted_elements[len(elements) // 2 - 1]) / 2.0
    return median_value


def quartile(elements: tuple) -> float | int:
    """quartile(elements: tuple) -> any

    Args:
        elements (tuple): tuple of numbers

    Returns:
        float | int: quartile of elements
    """
    sorted_elements = sorted(elements)
    quartile_values = [
        sorted_elements[len(elements) // 4],
        sorted_elements[len(elements) * 3 // 4]]
    quartile_values = list(map(float, quartile_values))
    return quartile_values


def std(elements: tuple) -> float | int:
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


def var(elements: tuple) -> float | int:
    """var(elements: tuple) -> float

    Args:
        elements (tuple): tuple of numbers

    Returns:
        float | int: variance of elements
    """
    elements_mean = mean(elements)
    deviation = list(map(lambda x: x - elements_mean, elements))
    variance = sum(list(map(lambda x: x ** 2, deviation))) / len(deviation)
    return variance


def main():
    pass


if __name__ == "__main__":
    main()
