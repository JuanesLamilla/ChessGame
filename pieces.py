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
        Piece.__init__(colour)
        self._start = True

    def check_valid_move(self, current_location: tuple[int, int],
                         attempted_location: tuple[int, int]) -> bool:
        """If the pawn has yet to move, return true if the attempted_location
        is one or two spaces forward. If the pawn has already moved, return
        true if the attempted_location is only one space forward.
        Return false otherwise."""

        if current_location[0] == attempted_location[0]:
            if self._start and\
                        current_location[1] == (attempted_location[1] - 2):
                    return True
            elif current_location[1] == (attempted_location[1] - 1):
                return True
        return False

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
        Piece.__init__(colour)

    def check_valid_move(self, current_location: tuple[int, int],
                         attempted_location: tuple[int, int]) -> bool:
        """Return true iff the attempted_location is two spaces in any
        direction and the one space to either side. Return false otherwise."""

        # Checks above and to both sides
        if attempted_location[1] == current_location[1] + 2 and \
                (attempted_location[0] == current_location[0] + 1 or
                    attempted_location[0] == current_location[0] - 1):
                return True

        # Checks below and to both sides
        elif attempted_location[1] == current_location[1] - 2 and \
                (attempted_location[0] == current_location[0] + 1 or
                    attempted_location[0] == current_location[0] - 1):
                return True

        # Checks to the right and to up or down
        elif attempted_location[0] == current_location[0] + 2 and \
                (attempted_location[1] == current_location[1] + 1 or
                    attempted_location[1] == current_location[1] - 1):
                return True

        # Checks to the left and to up or down
        elif attempted_location[0] == current_location[0] - 2 and \
                (attempted_location[1] == current_location[1] + 1 or
                    attempted_location[1] == current_location[1] - 1):
                return True

        return False


class Rook(Piece):
    """A chess rook located on the chess board.

            === Inherited Attributes ===
            colour:
                The colour of the chess piece. Can either be 'B' or 'W'.
            """

    colour: str

    def __init__(self, colour: str) -> None:
        Piece.__init__(colour)

    def check_valid_move(self, current_location: tuple[int, int],
                         attempted_location: tuple[int, int]) -> bool:
        """Return true iff attempted_location is on the same x or y plane
        as current_location."""

        if current_location[0] == attempted_location[0] or \
                current_location[1] == attempted_location[1]:
            return True
        return False


class Bishop(Piece):
    """A chess bishop located on the chess board.

            === Inherited Attributes ===
            colour:
                The colour of the chess piece. Can either be 'B' or 'W'.
            """

    colour: str

    def __init__(self, colour: str) -> None:
        Piece.__init__(colour)

    def check_valid_move(self, current_location: tuple[int, int],
                         attempted_location: tuple[int, int]) -> bool:
        """Return true iff attempted_location is diagonal on the board
        to current_location. Return False otherwise."""

        change_x = int(sqrt(current_location[0] - attempted_location[0])**2)
        change_y = int(sqrt(current_location[1] - attempted_location[1])**2)

        if change_x == change_y:
            return True
        return False


class Queen(Piece):
    """A chess queen located on the chess board.

            === Inherited Attributes ===
            colour:
                The colour of the chess piece. Can either be 'B' or 'W'.
            """

    colour: str

    def __init__(self, colour: str) -> None:
        Piece.__init__(colour)

    def check_valid_move(self, current_location: tuple[int, int],
                         attempted_location: tuple[int, int]) -> bool:
        """Return true iff attempted_location is diagonal on the board
        or one space in any direction from current_location.
        Return false otherwise."""

        change_x = int(sqrt(current_location[0] - attempted_location[0])**2)
        change_y = int(sqrt(current_location[1] - attempted_location[1])**2)

        if change_x == change_y:
            return True
        elif current_location[0] == attempted_location[0] and \
                (current_location[1] + 1 == attempted_location[1] or
                 current_location[1] - 1 == attempted_location[1]):
            return True
        elif current_location[1] == attempted_location[1] and \
                (current_location[0] + 1 == attempted_location[0] or
                 current_location[0] - 1 == attempted_location[0]):
            return False


class King(Piece):
    """A chess king located on the chess board.

            === Inherited Attributes ===
            colour:
                The colour of the chess piece. Can either be 'B' or 'W'.
            """

    colour: str

    def __init__(self, colour: str) -> None:
        Piece.__init__(colour)

    def check_valid_move(self, current_location: tuple[int, int],
                         attempted_location: tuple[int, int]) -> bool:
        """Return true iff attempted_location is one space away from
        current_location in any direction."""
        if current_location[0] - 1 <= \
                attempted_location[0] <= current_location[0] + 1 and \
                current_location[1] - 1 <= \
                attempted_location[1] <= current_location[1] + 1:
            return True
        return False
