from abc import ABC, abstractmethod


class Character(ABC):
    """Abstract base class for characters"""
    @abstractmethod
    def is_alive(self) -> bool:
        """Check if the character is alive"""
        pass

    @abstractmethod
    def die(self):
        """Kill the character"""
        pass


class Stark(Character):
    """Represent a character"""

    def __init__(self, name: str, is_alive: bool =True):
        """Initialize the character"""
        self.name = name
        self.is_alive = is_alive

    def is_alive(self) -> bool:
        """Return True if the character is alive otherwise return False"""
        return self.is_alive

    def die(self):
        """Set the character's alive status to False"""
        self.is_alive = False
