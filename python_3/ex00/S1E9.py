from abc import ABC, abstractmethod


class Character(ABC):
    """
    class Character(ABC)
    abstract class Character
    Args:
    ABC (_type_): Abstract Base Class need to make abatract class
    """

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        """
        Constructor
        Character(first_name, is_alive=True)
        Args:
            first_name (string): character first name
            is_alive (bool, optional): set status character alive.\
            Defaults to True.
        """
        pass

    @abstractmethod
    def die(self):
        """ virtual function die() """
        pass


class Stark(Character):
    """
    Stark(Character)
    inhereted class from Character (Abstract Class)
    """

    def __init__(self, first_name, is_alive=True):
        """
        Constructor for Stark Class
        Args:
            first_name (string): set first_name
            is_alive (bool, optional): set Character live status.\
        Defaults to True.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """
        Stark method die()
        set is_alive False
        """
        self.is_alive = False


def main():
    """
    test function for Stark class
    """
    pass


if __name__ == "__main__":
    main()
