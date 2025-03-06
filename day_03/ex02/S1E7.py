from S1E9 import Character


class Baratheon(Character):
    """Represents a character from House Baratheon"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Baratheon character"""
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def __str__(self):
        """Return a string representation of the Baratheon character"""
        return f"{self.family_name}, {self.eyes}, {self.hairs}"

    def __repr__(self):
        """Return a technical representation of
        the Baratheon character"""
        return (f"Vector: ('{self.family_name}', "
                f"'{self.eyes}', '{self.hairs}')>")


class Lannister(Character):
    """Represents a character from House Lannister"""

    def __init__(self, name: str, is_alive: bool = True):
        """Initialize a Lannister character"""
        super().__init__(name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    @classmethod
    def create_lannister(cls, name: str, is_alive: bool = True):
        """Create a new Lannister character"""
        return cls(name, is_alive)

    def __str__(self):
        """Return a string representation of the Lannister character"""
        return f"{self.family_name}, {self.eyes}, {self.hairs}"

    def __repr__(self):
        """Return a technical representation of
        the Lannister character"""
        return f"Vector: ('{self.family_name}', '{self.eyes}', '{self.hairs}')"
