class calculator:
    """
    Do calculations (addition, multiplication,
    subtraction, division) of vector with a scalar.
    """
    def __init__(self, vector):
        """
        Initializes object with the provided vector.
        """
        self.vector = vector

    def __add__(self, scalar):
        """Addition of a vector with a scalar."""
        self.vector = [x + scalar for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __mul__(self, scalar):
        """Multiplication of a vector with a scalar."""
        self.vector = [x * scalar for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __sub__(self, scalar):
        """Subtraction of a scalar from a vector."""
        self.vector = [x - scalar for x in self.vector]
        print(self.vector)
        return [x for x in self.vector]

    def __truediv__(self, scalar):
        """Division of a vector by a scalar."""
        try:
            self.vector = [x / scalar for x in self.vector]
            print(self.vector)
            return [x for x in self.vector]
        except ZeroDivisionError as error:
            print(ZeroDivisionError.__name__ + ":", error)

    def __repr__(self):
        return f"calculator({self.vector})"
