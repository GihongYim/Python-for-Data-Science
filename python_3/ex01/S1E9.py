from abc import ABC, abstractmethod


class Character(ABC):
    """Your docstring for Class"""

    @abstractmethod
    def __init__(self, first_name, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive
        # your code here
        pass

    @abstractmethod
    def die(self):
        pass


class Stark(Character):
    """Your docstring for Class"""
    # your code here

    def __init__(self, first_name, is_alive=True):
        """Your docstring for Constructor"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Your docstring for Method"""
        self.is_alive = False


def main():
    pass


if __name__ == "__main__":
    main()