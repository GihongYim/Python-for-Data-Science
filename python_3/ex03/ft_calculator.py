class calculator:
    """Representing Calculator class """
    # your code here
    
    def __init__(self, object):
        # your code here
        self.object = object
        pass
    
    def __add__(self, object) -> None:
        # your code here
        self.object = list(map(lambda x: x + object, self.object))
        print(self.object)
        pass

    def __mul__(self, object) -> None:
        # your code here
        self.object = list(map(lambda x: x * object, self.object))
        print(self.object)
        pass

    def __sub__(self, object) -> None:
        # your code here
        self.object = list(map(lambda x: x - object, self.object))
        print(self.object)
        pass

    def __truediv__(self, object) -> None:
        # your code here
        try:
            self.object = list(map(lambda x: x / object, self.object))
            print(self.object)
        except ZeroDivisionError as e:
            print(f"{e} : not dividev by zero")
        pass
