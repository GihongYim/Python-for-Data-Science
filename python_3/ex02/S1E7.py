from S1E9 import Character


class Baratheon(Character):
    """Representing the Baratheon family."""
    # your code here

    def __init__(self, first_name, is_alive=True):
        # your code here
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = 'Barath'
        self.eyes = 'brown'
        self.hairs = 'dark'
    
    def die(self):
        self.is_alive = False
        # return not self.is_alive
    
    def __str__(self):
        return "{}, {}, {}".format(self.family_name, self.eyes, self.hairs)
    
    def __repr__(self):
        return "Vector: ('{}', '{}', '{}')".format(self.family_name, self.eyes, self.hairs)


class Lannister(Character):
    """docstring for Lannister Class"""
    
    def __init__(self, first_name, is_alive=True):
        # your code here
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'
    
    def die(self):
        """Lannister die"""
        return not self.is_alive
    
    def __str__(self):
        return "{}, {}, {}".format(self.family_name, self.eyes, self.hairs)
    
    def __repr__(self):
        return "Vector: ('{}', '{}', '{}')".format(self.family_name, self.eyes, self.hairs)

    # decorator
    @classmethod
    def create_lannister(self, first_name, is_alive):
        """create_lannister : make new lannister"""
        # your code here
        return Lannister(first_name, is_alive)
