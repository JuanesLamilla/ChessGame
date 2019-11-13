import pieces
import numpy as np


class Board(object):
    """
    The chess board where the piece movement will occur.

    === Public Attributes ===
    curTurn:
        Represents the player who has the current move. ('B' or 'W')
    board:
        Represents the game board in a 8x8 Python list.
    """

    def __init__(self):
        """
        Initializes the Chess Board to value self.board.
        The first player to begin the game will be 'W'.
        """
        self.cur_turn = 'W'
        self.board = self.create_board()


    def get_valid_moves(self, coordinate):
        """
        Returns a list of valid moves for the piece at a given coordinate
        """
        cur_x = coordinate[0]
        cur_y = coordinate[1]

        #if user tries to choose empty piece
        if self.board[cur_x][cur_y] == 0:
            raise ValueError("Please select a tile with your piece.")

        #if user tries to chose other player's piece
        if self.board[cur_x][cur_y].colour != self.cur_turn:
            raise ValueError("Please select your piece only")

        #other cases #TODO


    def move(self, old_coord, new_coord):
        """
        Moves the piece from cur_coord (x, y) to new_coord (x, y).
        """
        old_x = old_coord[0]
        old_y = old_coord[1]

        new_x = new_coord[0]
        new_y = new_coord[1]

        self.board[new_x][new_y] = self.board[old_x][old_y]
        self.board[old_x][old_y] = 0

    def __repr__(self):
        """
        Prints the Chess Board in matrix format.
        Utilized numpy array to format 2d list to matrix format
        """
        return str(np.matrix(self.board))


    def create_board(self):
        """
        Creates the initial game board required for Chess.
        Populated spaces are filled with respective pieces from pieces.py.
        Vacant spaces are filled with 0s.

        #TODO replace the strings with actual pieces from the pieces class
        """

        board = [[0 for y in range(8)] for x in range(8)]

        #Placing the Rooks

        board[0][0] = pieces.Rook('B')
        board[0][7] = pieces.Rook('B')
        board[7][0] = pieces.Rook('W')
        board[7][7] = pieces.Rook('W')

        #Placing the Knights

        board[0][1] = pieces.Knight('B')
        board[0][6] = pieces.Knight('B')
        board[7][1] = pieces.Knight('W')
        board[7][6] = pieces.Knight('w')

        #Placing the Bishops

        board[0][2] = pieces.Bishop('B')
        board[0][5] = pieces.Bishop('B')
        board[7][2] = pieces.Bishop('W')
        board[7][5] = pieces.Bishop('W')

        #Placing the Queens
        board[0][3] = pieces.Queen('B')
        board[7][3] = pieces.Queen('w')

        #Placing the Kings
        board[0][4] = pieces.King('B')
        board[7][4] = pieces.King('W')

        #Placing the Pawns

        for i in range(8):
            board[1][i] = pieces.Pawn('B')
            board[6][i] = pieces.Pawn('W')

        return board


#For Testing
if __name__ == '__main__':
    chess_board = Board()

    #Moving pawn two spaces
    chess_board.move((6,0), (4,0))

    print(isinstance(chess_board.board[4][0], pieces.Pawn))
    print(chess_board.board[4][0].colour)

    #print(repr(chess_board))
