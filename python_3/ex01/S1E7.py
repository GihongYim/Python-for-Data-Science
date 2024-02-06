from S1E9 import Character


class Baratheon(Character):
    """Baratheon Class inhereted from Character class"""

    def __init__(self, first_name, is_alive=True):
        """
    Constructor Baratheon class

    Args:
        first_name (string): first_name
        is_alive (bool, optional): set Character alive status true.\
            Defaults to True.
        """
        self.firat_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Baratheon'
        self.eyes = 'brown'
        self.hairs = 'dark'

    def die(self):
        """
    Set Character class instance is_alive status False
        """
        self.is_alive = False

    def __str__(self):
        """
        return string information about Baratheon attribute

        Returns:
            string: "{}, {}, {}".format(self.family_name, self.eyes,\
                self.hairs)
        """
        return "{}, {}, {}".format(self.family_name, self.eyes, self.hairs)

    def __repr__(self):
        """
        representation for Baratheon Class instance
        Returns:
            string: "Vector: ('{}', '{}', '{}')".format(self.family_name,\
                self.eyes, self.hairs)
        """
        return "Vector: ('{}', '{}', '{}')".format(self.family_name,
                                                   self.eyes,
                                                   self.hairs)


class Lannister(Character):
    """
    Lannister class inhereted from Character
    """

    def __init__(self, first_name, is_alive=True):
        """
        Constructor of Lannister class

        Args:
            first_name (_type_): first_name
            is_alive (bool, optional): is_alive -> default = True
        """
        self.first_name = first_name
        self.is_alive = is_alive
        self.family_name = 'Lannister'
        self.eyes = 'blue'
        self.hairs = 'light'

    def die(self):
        """
           Set Character class instance is_alive status False

        Returns:
            : _description_
        """
        self.is_alive = False

    def __str__(self):
        """
            return string information about Lannister attribute

        Returns:
            string: "{}, {}, {}".format(self.family_name,\
                self.eyes, self.hairs)
        """

        return "{}, {}, {}".format(self.family_name,
                                   self.eyes,
                                   self.hairs)

    def __repr__(self):
        """
        representation for Lannister Class instance
        Returns:
            string: "Vector: ('{}', '{}', '{}')".format(self.family_name,\
                self.eyes, self.hairs)
        """

        return "Vector: ('{}', '{}', '{}')".format(self.family_name,
                                                   self.eyes,
                                                   self.hairs)

    @classmethod
    def create_lannister(self, first_name, is_alive):
        """

        Args:
            first_name (string): Lannister's first_name
            is_alive (bool): set Lannister

        Returns:
            Lannister instance: return Lannister instance
        """

        return Lannister(first_name, is_alive)
