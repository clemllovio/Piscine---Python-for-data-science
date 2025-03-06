from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Represents a King"""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a King character"""
        super().__init__(first_name, is_alive)

    def set_eyes(self, new_eyes):
        """Change eye color"""
        if new_eyes:
            self.eyes = new_eyes

    def get_eyes(self):
        """Return eye color"""
        return self.eyes

    def set_hairs(self, new_hairs):
        """Change hair color"""
        if new_hairs:
            self.hairs = new_hairs

    def get_hairs(self):
        """Return hair color"""
        return self.hairs
