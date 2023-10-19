import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass()
class Student:
    """Representing Student Class"""
    name: str
    surname: str
    active: bool
    login: str = field(kw_only=True)
    id: str = field(kw_only=True)
    
    def __init__(self, name: str, surname: str, active: bool = True):
        self.name = name
        self.surname = surname
        self.active = active
        self.login = name[0] + surname
        self.id = generate_id()
    

def main():
    pass
   

if __name__ == "__main__":
    main()