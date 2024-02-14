class calculator:
    """calculator class
    for vector calculation
    """

    @staticmethod
    def _check_samesize(V1: list[float], V2: list[float]) -> None:
        if len(V1) != len(V2):
            raise ValueError("Vectors must have identical sizes")

    @staticmethod
    def _check_samesize_decorator(func):
        def wrapper(*args, **kwargs):
            calculator._check_samesize(args[1], args[2])
            return func(*args, **kwargs)
        return wrapper

    @classmethod
    @_check_samesize_decorator
    def dotproduct(cls, V1: list[float], V2: list[float]) -> None:
        """
        dot(inner) product for two vector V1, V2

        Args:
            V1 (list[float]): left 1-dim vector
            V2 (list[float]): right1 1-dim vector
        """
        V1 = map(float, V1)
        V2 = map(float, V2)
        dotproduct_result = sum(list(map((lambda x, y: x * y), V1, V2)))
        print("Dot product is: ", dotproduct_result)
        return None

    @classmethod
    @_check_samesize_decorator
    def add_vec(cls, V1: list[float], V2: list[float]) -> None:
        """
        vector addition for two vector V1, V2

        Args:
            V1 (list[float]): left 1-dim vector
            V2 (list[float]): right1 1-dim vector
        """
        V1 = map(float, V1)
        V2 = map(float, V2)
        add_vec_result = list(map((lambda x, y: x + y), V1, V2))
        print("Add Vector is :", add_vec_result)
        return None

    @classmethod
    @_check_samesize_decorator
    def sous_vec(cls, V1: list[float], V2: list[float]) -> None:
        """
        vector subtraction for two vector V1, V2
        Args:
            V1 (list[float]): left 1-dim vector
            V2 (list[float]): right1 1-dim vector
        """
        V1 = map(float, V1)
        V2 = map(float, V2)
        sous_vec_result = list(map((lambda x, y: x - y), V1, V2))
        print("Sous Vector is :", sous_vec_result)
        return None


def main():
    pass


if __name__ == "__main__":
    main()
