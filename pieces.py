class Piece:
    """A chess piece located on the chess board.

        === Public Attributes ===
        colour:
            The colour of the chess piece. Can either be 'B' or 'W'.
        """
    colour: str

    def __init__(self, colour: str) -> None:
        """Initialize a new Piece with a given colour.
        """
        self.colour = colour

    def check_valid_move(self, current_location: tuple[int, int],
                         attempted_location: tuple[int, int]) -> bool:
        """Returns true iff the attempted move for the piece is valid.
        For both current_location and attempted_location,
        .._location[0] is the x coordinate and
        .._location[1] is the y coordinate.
        """
    raise NotImplementedError
