class calculator:
    """ calculator class
    """

    def __init__(self, object):
        """_summary_

        Args:
            object (_type_): _description_
        """
        self.object = object
        pass

    def __add__(self, object) -> None:
        """_summary_
        """
        self.object = list(map(lambda x: x + object, self.object))
        print(self.object)
        return None

    def __mul__(self, object) -> None:
        """_summary_

        Args:
            object (_type_): _description_
        """
        self.object = list(map(lambda x: x * object, self.object))
        print(self.object)
        return None

    def __sub__(self, object) -> None:
        """_summary_

        Args:
            object (_type_): _description_
        """
        self.object = list(map(lambda x: x - object, self.object))
        print(self.object)
        return None

    def __truediv__(self, object) -> None:
        """_summary_

        Args:
            object (_type_): _description_
        """
        try:
            self.object = list(map(lambda x: x / object, self.object))
            print(self.object)
        except ZeroDivisionError as e:
            print(f"{e} : not dividev by zero")
        return None
