from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """This class represents King Joffrey Baratheon,
    inheriting from both Baratheon and Lannister."""
    def __init__(self, first_name, is_alive=True):
        """Initialize the King with
        the characteristics from both families."""
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """Set the eye color of the King."""
        self.eyes = color

    def set_hairs(self, color):
        """Set the haur color of the King."""
        self.hairs = color

    def get_eyes(self):
        """Get the eye color of the King."""
        return self.eyes

    def get_hairs(self):
        """Get the hair color of the King."""
        return self.hairs
