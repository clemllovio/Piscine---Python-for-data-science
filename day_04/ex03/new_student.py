import random
import string
from dataclasses import dataclass, field


def generate_id() -> str:
    """Generates a random 15-character string
    consisting of lowercase letters."""
    return "".join(random.choices(string.ascii_lowercase, k=15))


@dataclass
class Student:
    """A class representing a student."""
    name: str = field(init=True)
    surname: str = field(init=True)
    active: bool = field(init=False, default=True)
    login: str = field(init=False, default=None)
    id: str = field(init=False, default=generate_id())

    def __post_init__(self):
        """ Initializes the login attribute by concatenating
        the first letter of the name and the surname."""
        try:
            self.login = self.name[0] + self.surname
        except Exception as e:
            print(f"typeError: {e}")
