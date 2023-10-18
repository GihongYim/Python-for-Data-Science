from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """representing King class"""
    def __init__(self, first_name, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
    
    def set_eyes(self, eyes):
        self.eyes = eyes
    
    def set_hairs(self, hairs):
        self.hairs = hairs
    
    def get_eyes(self):
        return self.eyes
    
    def get_hairs(self):
        return self.hairs