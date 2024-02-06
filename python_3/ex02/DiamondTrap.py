from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    King(Baratheon, Lannister)

    Args:
        Baratheon (Character): class
        Lannister (Character): class
    """
    def __init__(self, first_name, is_alive=True):
        """King.__init__

        Args:
            first_name (str): King's first name
            is_alive (bool, True): set default is_alive. Defaults to True.
        """
        super().__init__(first_name, is_alive)

    def set_eyes(self, eyes) -> str:
        """set_eyes

        Args:
            eyes (str): eye color
        """
        self.eyes = eyes

    def set_hairs(self, hairs) -> str:
        """set_hairs

        Args:
            hairs (str): set hair color
        """
        self.hairs = hairs

    def get_eyes(self) -> str:
        """get_eyes

        Returns:
            str | None: eyes color
        """
        return self.eyes

    def get_hairs(self) -> str:
        """get_hairs

        Returns:
            str: return color of hair
        """
        return self.hairs

    def __repr__(self):
        """
        representation for King Class instance
        Returns:
            string: "Vector: ('{}', '{}', '{}')".format(self.family_name,\
                self.eyes, self.hairs)
        """
        return "Vector: ('{}', '{}', '{}')".format(self.family_name,
                                                   self.eyes,
                                                   self.hairs)


def main():
    pass


if __name__ == "__main__":
    main()
