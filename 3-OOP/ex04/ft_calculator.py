class calculator:
    """
    Do calculations (addition, multiplication,
    subtraction, division) of vector with a scalar.
    """
    def __init__(self, vector):
        """Initializes object with the provided vector."""
        self.vector = vector

    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> float:
        """Calculate the dot product of two vectors."""
        res = sum(x * y for x, y in zip(V1, V2))
        print(f"Dot product is: {res}")
        return res

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> list[float]:
        """Add two vectors element-wise."""
        res = [x + y for x, y in zip(V1, V2)]
        print(f"Add Vector is: {res}")
        return [x + y for x, y in zip(V1, V2)]

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> list[float]:
        """Subtract two vectors element-wise."""
        res = [x - y for x, y in zip(V1, V2)]
        print(f"Sous Vector is: {res}")
        return res
    