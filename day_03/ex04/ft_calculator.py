class calculator:
    """A class to perform vector operations on a list of numbers (vector)
    The operations include dot product, addition, subtraction"""

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """Performs and prints the dot product of two vectors"""
        try:
            result = sum(V1[i] * V2[i] for i in range(len(V1)))
            print(f'Dot product: {result}')
        except TypeError as e:
            print(f"TypeError: {e}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """Performs and prints the sum of two vectors"""
        try:
            result = [format(x + y, '.1f') for x, y in zip(V1, V2)]
            print(f'Add Vector is : {result}')
        except TypeError as e:
            print(f"TypeError: {e}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """Performs and prints the subtraction of two vectors"""
        try:
            result = [format(x - y, '.1f') for x, y in zip(V1, V2)]
            print(f'Sous Vector is : {result}')
        except TypeError as e:
            print(f"TypeError: {e}")
