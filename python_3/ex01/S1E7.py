from S1E9 import Character


class Baratheon(Character):
    """docstring for Baratheon Class"""
    # your code here
    def __init__(self, first_name, is_alive=True):
        # your code here
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'
    
    def die(self):
        return not self.is_alive
    
    def __str__(self):
        return ""


class Lannister(Character):
    """docstring for Lannister Class"""
    
    def __init__(self, first_name, is_alive=True):
        # your code here
        self.first_name = first_name
        self.is_alive = is_alive
    
    def die(self):
        """Lannister die"""
        return not self.is_alive

    # decorator
    def create_lannister(self, first_name, is_alive):
        """create_lannister : make new lannister"""
        # your code here
        return Lannister(first_name, is_alive)
