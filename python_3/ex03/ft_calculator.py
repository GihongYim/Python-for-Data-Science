class calculator:
    """ calculator class
    """

    def __init__(self, object):
        """calculator.__init__"""
        try:
            assert all(isinstance(num, int | float) for num in object), \
                "element in list not int or float"
        except Exception as e:
            print(f"{e.__class__.__name__}: {e}")
            exit()
        self.object = object
        pass

    def __add__(self, object) -> None:
        """calculator.__add__
        Args:
            object (_type_): addition
        """
        self.object = list(map(lambda x: x + object, self.object))
        print(self.object)
        return None

    def __mul__(self, object) -> None:
        """calculator.__mul__

        Args:
            object (_type_): multiply
        """
        self.object = list(map(lambda x: x * object, self.object))
        print(self.object)
        return None

    def __sub__(self, object) -> None:
        """calculator.__sub__

        Args:
            object (_type_): subtract
        """
        self.object = list(map(lambda x: x - object, self.object))
        print(self.object)
        return None

    def __truediv__(self, object) -> None:
        """calculator.__truediv__

        Args:
            object (_type_): division
        """
        try:
            self.object = list(map(lambda x: x / object, self.object))
            print(self.object)
        except ZeroDivisionError as e:
            print(f"{e} : not dividev by zero")
        return None


def main():
    pass


if __name__ == "__main__":
    main()
