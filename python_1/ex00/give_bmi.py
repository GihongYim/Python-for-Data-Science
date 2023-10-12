def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    #your code here
    bmis = [person_weight / (person_height ** 2) for person_height, person_weight in zip(height, weight)]
    return bmis

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
#your code here
    above_limit = [x > limit for x in bmi]
    return above_limit


def main():
    # your tests and your error handling
    pass


if __name__ == "__main__":
    main()
