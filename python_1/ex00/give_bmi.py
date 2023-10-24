def give_bmi(height: list[int | float], weight: list[int | float])\
        -> list[int | float]:
    """_summary_
        calculate bmi for each element

    Args:
        height: list[int | float]
        weight: list[int | float]

    Returns:
        list[int | float]: each bmis
    """
    bmis = [person_weight / (person_height ** 2)
            for person_height, person_weight in zip(height, weight)]
    return bmis


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """_summary_
        check bmi greater than limit
    Args:
        bmi (list[int  |  float]): _description_
        limit (int): _description_

    Returns:
        list[bool]: _description_
    """
    above_limit = [x > limit for x in bmi]
    return above_limit


def main():
    """
    _summary_
        test function for give_bmi function
        default pass
    """
    pass


if __name__ == "__main__":
    main()
