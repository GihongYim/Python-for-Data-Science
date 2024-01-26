def give_bmi(height: list[int | float], weight: list[int | float])\
      -> list[int | float]:
    """_summary_

    Args:
        height (list[int  |  float]): height(m) list
        weight (list[int  |  float]): weight(kg) list

    Returns:
        list[int | float]: return bmi list
    """
    try:
        assert len(height) == len(weight), "height, weight size not equal"
        assert all(isinstance(element, int | float) for element in height), \
            "height element are not int or str"
        assert all(isinstance(element, int | float) for element in weight), \
            "weight element are not int or str"
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        exit()

    bmi_list = [(person_weight / (person_height ** 2))
                for person_height, person_weight in zip(height, weight)]
    return bmi_list


def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    """_summary_

    Args:
        bmi (list[int  |  float]): _description_
        limit (int): _description_

    Returns:
        list[bool]: _description_
    """
    try:
        assert all(isinstance(element, int | float) for element in bmi), \
            "bmi element are not int or str"
        assert isinstance(limit, int), "limit not int"
    except Exception as e:
        print(f"{e.__class__.__name__}: {e}")
        exit()
    limit_list = [person_bmi >= limit for person_bmi in bmi]
    return limit_list


def main():
    pass


if __name__ == "__main__":
    main()
