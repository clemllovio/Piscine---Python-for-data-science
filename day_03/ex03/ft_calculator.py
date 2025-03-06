class calculator:
    """A class to perform arithmetic operations on a list of numbers (vector)
    The operations include addition, subtraction,
    multiplication, and division"""

    def __init__(self, vector: list[float]) -> None:
        """Initializes the Calculator with a list of numbers (vector)."""
        self.vector = vector

    def __add__(self, object) -> None:
        """Performs addition of the vector and the given object"""
        try:
            self.vector = [item + object for item in self.vector]
            print(self.vector)
        except TypeError as e:
            print(f"TypeError: {e}")

    def __mul__(self, object) -> None:
        """Performs multiplication of the vector and the given object"""
        try:
            self.vector = [item * object for item in self.vector]
            print(self.vector)
        except TypeError as e:
            print(f"TypeError: {e}")

    def __sub__(self, object) -> None:
        """Performs subtraction of the vector and the given object"""
        try:
            self.vector = [item - object for item in self.vector]
            print(self.vector)
        except TypeError as e:
            print(f"TypeError: {e}")

    def __truediv__(self, object) -> None:
        """Performs division of the vector by the given object"""
        try:
            self.vector = [item / object for item in self.vector]
            print(self.vector)
        except ZeroDivisionError as e:
            print(f"ZeroDivisionError: {e}")
        except TypeError as e:
            print(f"TypeError: {e}")
