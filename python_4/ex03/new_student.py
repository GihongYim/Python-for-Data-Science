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
    login: str
    id: str
    """
    name: str
    surname: str
    active: bool
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    def __init__(self, name: str, surname: str, active: bool = True):
        """__init__

        Args:
            name (str): student name
            surname (str): surname of student
            active (bool, optional): student active. Defaults to True.
        """

        try:
            assert isinstance(name, str), "name value is not str"
            assert isinstance(surname, str), "surname value is not str"
            assert name != "", "name is empty"
            assert surname != "", "surname is empty"
        except Exception as e:
            print(f"{e.__class__.__name__}: {e}")
            exit(1)
        self.name = name
        self.surname = surname
        self.active = active
        self.login = name[0] + surname


def main():
    pass


if __name__ == "__main__":
    main()
