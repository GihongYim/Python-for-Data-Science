def ft_filter(function, iterable) -> filter:
    """ft_filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true.
    """
    if function is None:
        result = [item for item in iterable if iterable]
    else:
        result = [item for item in iterable if function(item)]
    return iter(result)


def func(x):
    if x == 3:
        return True
    else:
        return False


def main():
    """_summary_
    """
    # print(ft_filter.__doc__)
    arr = [1, 2, 3, 4, 5]
    arr2 = ft_filter(func, arr)
    arr3 = filter(func, arr)
    for element in arr2:
        print(element)
    for element in arr3:
        print(element)


if __name__ == "__main__":
    main()
