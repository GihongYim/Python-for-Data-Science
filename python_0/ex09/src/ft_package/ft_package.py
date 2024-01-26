def count_in_list(elements: list, target: any) -> int:
    count = 0

    for element in elements:
        if element == target:
            count += 1
    return count
