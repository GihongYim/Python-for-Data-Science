import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """generate_id() -> str

    Returns:
        str: random_id
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass()
class Student:
    """
    class Student
    name: str
    surname: str
    active: bool
    login: str = field(kw_only=True)
    id: str = field(kw_only=True)
    """
    name: str
    surname: str
    active: bool
    login: str = field(kw_only=True)
    id: str = field(kw_only=True)

    def __init__(self, name: str, surname: str, active: bool = True):
        """__init__

        Args:
            name (str): student name
            surname (str): surname of student
            active (bool, optional): student active. Defaults to True.
        """
        if name == "":
            print("Error: name is empty string")
            exit()
        if surname == "":
            print("Error: surname is empty string")
            exit()
        self.name = name
        self.surname = surname
        self.active = active
        self.login = name[0] + surname
        self.id = generate_id()


def main():
    pass


if __name__ == "__main__":
    main()
