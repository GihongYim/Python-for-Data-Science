def count_in_list(elements: list, target: any) -> int:
    """_summary_
    Args:
        elements (list): elements
        target (any): target element for matching elements

    Returns:
        int: _description_
    """
    count = 0

    for element in elements:
        if element == target:
            count += 1
    return count
