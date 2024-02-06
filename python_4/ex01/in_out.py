def square(x: int | float) -> int | float:
    """square(x: int | float) -> int | float

    Args:
        x (int | float): base of power

    Returns:
        int | float: x square 2
    """
    return x ** 2


def pow(x: int | float) -> int | float:
    """pow(x: int | float) -> int | float

    Args:
        x (int | float): base of power

    Returns:
        int | float: x power of x
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """outer(x: int | float, function) -> object

    Args:
        x (int | float): function input
        function (_type_): return function store x

    Returns:
        object: function calculate power
    """
    count = None

    def inner() -> float:
        """inner() -> float

        Returns:
            float: calculate function()
        """
        nonlocal count
        if count is None:
            count = function(x)
        else:
            count = function(count)
        return count
    return inner
