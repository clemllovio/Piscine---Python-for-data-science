from S1E9 import Character


class Baratheon(Character):
    """Represents a character from House Baratheon"""

    def __init__(self, name: str, is_alive: bool = True):
        """Initialize a character a Baratheon character"""
        super().__init__(name, is_alive)
        self.first_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def is_alive(self) -> bool:
        """Return True if the character is alive otherwise return False"""
        return self.is_alive

    def die(self):
        """Set the character's alive status to False"""
        self.is_alive = False

    def __str__(self):
        return f"{self.first_name}, {self.eyes}, {self.hairs}"

    def __repr__(self):
        return f"Vector <{self.first_name}, {self.eyes}, {self.hairs}>"

class Lannister(Character):

    def __init__(self, name: str, is_alive: bool = True):
        """Initialize a Lannister character"""
        super().__init__(name, is_alive)
        self.first_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def is_alive(self) -> bool:
        """Return True if the character is alive otherwise return False"""
        return self.is_alive

    def die(self):
        """Set the character's alive status to False"""
        self.is_alive = False

    @classmethod
    def create_lannister(cls, name: str, is_alive: bool = True):
        return cls(name, is_alive)

    def __str__(self):
        return f"{self.first_name}, {self.eyes}, {self.hairs}"

    def __repr__(self):
        return f"Vector <{self.first_name}, {self.eyes}, {self.hairs}>"