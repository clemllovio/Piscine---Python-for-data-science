from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class for characters"""
    @abstractmethod
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a new character"""
        self.first_name = first_name
        self.is_alive = is_alive

    def die(self):
        """Set the character's alive status to False"""
        self.is_alive = False


class Stark(Character):
    """Represents a character from House Stark"""

    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize a Stark character"""
        super().__init__(first_name, is_alive)
