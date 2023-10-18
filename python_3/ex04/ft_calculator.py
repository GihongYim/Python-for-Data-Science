class calculator:
    # your code here

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        # your code here
        V1 = map(float, V1)
        V2 = map(float, V2)
        dotproduct_result = sum(list(map((lambda x, y: x * y), V1, V2)))
        print("Dot product is: ", dotproduct_result)

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        # your code here
        V1 = map(float, V1)
        V2 = map(float, V2)
        add_vec_result = list(map((lambda x, y: x + y), V1, V2))
        print("Add Vector is :", add_vec_result)
        pass
    
    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        # your code here
        V1 = map(float, V1)
        V2 = map(float, V2)
        sous_vec_result = list(map((lambda x, y: x - y), V1, V2))
        print("Sous Vector is :", sous_vec_result)
        pass