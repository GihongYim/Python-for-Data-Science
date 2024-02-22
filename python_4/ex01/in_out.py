def square(x: int | float) -> int | float:
    """square(x: int | float) -> int | float

    Args:
        x (int | float): base of power

    Returns:
        int | float: x square 2
    """
    try:
        if not isinstance(x, int | float):
            raise TypeError(f"{x} is not an numerical")
        result = x ** 2
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        exit(1)
    return result


def pow(x: int | float) -> int | float:
    """pow(x: int | float) -> int | float

    Args:
        x (int | float): base of power

    Returns:
        int | float: x power of x
    """
    try:
        if not isinstance(x, int | float):
            raise TypeError(f"{x} is not an numerical")
        result = x ** x
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        exit(1)
    return result


def outer(x: int | float, function) -> object:
    """outer(x: int | float, function) -> object

    Args:
        x (int | float): function input
        function (_type_): return function store x

    Returns:
        object: function calculate power
    """
    count = 0

    def inner() -> float:
        """inner() -> float

        Returns:
            float: calculate function()
        """
        nonlocal count
        if count == 0:
            count = function(x)
        else:
            count = function(count)
        return count
    return inner
