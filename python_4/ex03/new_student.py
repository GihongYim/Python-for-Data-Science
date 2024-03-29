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
    active: bool = field(init=False, default=True)
    login: str = field(init=False)
    id: str = field(init=False, default=generate_id())

    def __post_init__(self):
        self.login = self.name[0] + self.surname


def main():
    pass


if __name__ == "__main__":
    main()
