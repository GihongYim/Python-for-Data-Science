def slice_me(family: list, start: int, end: int) -> list:
    #your code here
    array = []
    try:
        if type(family[0]) != list:
            raise AssertionError("AssertionError: family is not 2-dimensional array")
        if start >= len(family) or -start > len(family):
            raise IndexError("IndexError: start list index out of range")
        if end >= len(family) or -end > len(family):
            raise IndexError("IndexError: end list index out of range")
        row = len(family)
        column = len(family[0])
        print(f"My shape is : ({row}, {column})")
        array = family[start:end]
        new_row = len(array)
        new_column = len(array[0])
        print(f"My new shape is : ({new_row}, {new_column})")
    except Exception as e:
        print(e)
    return array

def main():
    pass

if __name__ == "__main__":
    main()