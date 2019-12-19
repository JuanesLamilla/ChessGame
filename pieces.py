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


class Pawn(Piece):
    """A chess pawn located on the chess board.

        === Private Attributes ===
        _start:
            True if the pawn has yet to make a move, False if it has moved.

        === Inherited Attributes ===
        colour:
            The colour of the chess piece. Can either be 'B' or 'W'.
        """

    colour: str
    _start: bool

    def __init__(self, colour: str) -> None:
        Piece.__init__(self, colour)
        self._start = True

    def made_first_move(self) -> None:
        self._start = False


class Knight(Piece):
    """A chess knight located on the chess board.

            === Inherited Attributes ===
            colour:
                The colour of the chess piece. Can either be 'B' or 'W'.
            """

    colour: str

    def __init__(self, colour: str) -> None:
        Piece.__init__(self, colour)


class Rook(Piece):
    """A chess rook located on the chess board.

            === Inherited Attributes ===
            colour:
                The colour of the chess piece. Can either be 'B' or 'W'.
            """

    colour: str

    def __init__(self, colour: str) -> None:
        Piece.__init__(self, colour)


class Bishop(Piece):
    """A chess bishop located on the chess board.

            === Inherited Attributes ===
            colour:
                The colour of the chess piece. Can either be 'B' or 'W'.
            """

    colour: str

    def __init__(self, colour: str) -> None:
        Piece.__init__(self, colour)


class Queen(Piece):
    """A chess queen located on the chess board.

            === Inherited Attributes ===
            colour:
                The colour of the chess piece. Can either be 'B' or 'W'.
            """

    colour: str

    def __init__(self, colour: str) -> None:
        Piece.__init__(self, colour)


class King(Piece):
    """A chess king located on the chess board.

            === Inherited Attributes ===
            colour:
                The colour of the chess piece. Can either be 'B' or 'W'.
            """

    colour: str

    def __init__(self, colour: str) -> None:
        Piece.__init__(self, colour)
