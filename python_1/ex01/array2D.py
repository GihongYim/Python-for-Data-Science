def slice_me(family: list, start: int, end: int) -> list:
    """_summary_
        slice family(list) start <= x < end for x in list index
    Args:
        family (list): original list
        start (int): start index for sliced list
        end (int): end index for sliced list (not included return list)

    Raises:
        AssertionError: family is not 2-dimensional array
        IndexError: start list index out of range
        IndexError: end list index out of range

    Returns:
        list: family[start, end)
    """

    array = []
    try:
        assert type(family[0]) is list, \
            "family is not 2-dimensional array"
        if start >= len(family) or -start > len(family):
            raise IndexError("start list index out of range")
        if end >= len(family) or -end > len(family):
            raise IndexError("end list index out of range")
        row = len(family)
        column = len(family[0])
        assert all(column == len(col) for col in family), \
            "column length are not equal"
        array = family[start:end]
        new_row = len(array)
        new_column = len(array[0])
        print(f"My shape is : ({row}, {column})")
        print(f"My new shape is : ({new_row}, {new_column})")
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        exit()
    return array


def main():
    """
    main function for slice_my.py test your own code here
    """
    arr = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5],
           [6, 6], [7, 7], [8, 8], [9, 9], [10, 10]]
    print(slice_me(arr, 2, 5))


if __name__ == "__main__":
    main()
