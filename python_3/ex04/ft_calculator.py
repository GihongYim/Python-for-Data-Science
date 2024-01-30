class calculator:
    """calculator class
    for vector calculation
    """

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
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

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
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
    
    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
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