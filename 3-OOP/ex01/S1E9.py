from abc import ABC, abstractmethod


class Character(ABC):
    """This is an abstract class for characters."""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize the character with a name and alive status."""
        self.first_name = first_name
        self.is_alive = is_alive


    @abstractmethod
    def die(self):
        """Change the alive status of the character to False."""
        pass


class Stark(Character):
    """This class represents a Stark character from GOT."""
    def __init__(self, first_name: str, is_alive: bool = True):
        """Initialize the Stark character with a name and alive status."""
        super().__init__(first_name, is_alive)


    def die(self):
        """Change the alive status of the Stark character to False."""
        self.is_alive = False
