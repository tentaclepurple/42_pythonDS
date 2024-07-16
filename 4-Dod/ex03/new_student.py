import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """
    Generate a random string of 15 characters
    """
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """ Student class """
    name: str
    surname: str
    active: bool = True
    login: str = field(init=False)
    id: str = field(init=False, default_factory=generate_id)

    def __post_init__(self):
        if not isinstance(self.name, str) or not isinstance(self.surname, str):
            raise TypeError("name and surname must be strings.")

        if not self.name.strip() or not self.surname.strip():
            raise ValueError("name and surname must not be empty.")

        self.login = self.name[0].lower() + self.surname.lower()
