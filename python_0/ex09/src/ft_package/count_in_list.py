def count_in_list(a, b):
    """
    count_in_list(a: collections, b: count_target) -> int
    """
    count = 0
    for element in b:
        if a == element:
            count += 1
    return count


def main():
    pass


if __name__ == "__main__":
    main()