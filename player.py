class Player:
    """
    represents a player in the chess game
    """
    def __init__(self, name):
        """
        initializes the chess player, with a given name,
        sets colour to white by default, set_colour method is used to change the
        players colour. players initialized as a human player.
        """
        self.name = name
        self.colour = "W"
        #type is for later use when implementing player vs. ai, set to human for now
        self.type = "human"

    def get_name(self) -> str:
        """
        return the name of the chess player.
        >>> player1 = Player("Bob")
        >>> player1.get_name()
        "Bob"
        """
        return self.name

    def get_colour(self) -> str:
        """
        return the colour of the chess player.
        >>> player1 = Player("Rob")
        >>> player1.get_colour()
        "W"
        """
        return self.colour

    def set_colour(self, colour) -> None:
        """
        sets the colour of the chess player, either "W" for white
        or "B" for black.
        >>> player1 = Player("John")
        >>> player1.get_colour()
        "W"
        >>> player1.set_colour("B")
        >>> player1.get_colour()
        "B"
        """
        self.colour = colour
