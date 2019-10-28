#import pieces
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
        #TODO Implement wrt. Pieces class

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

        board[0][0] = 'B_R'
        board[0][7] = 'B_R'
        board[7][0] = 'W_R'
        board[7][7] = 'W_R'

        #Placing the Knights

        board[0][1] = 'B_Kn'
        board[0][6] = 'B_Kn'
        board[7][1] = 'W_Kn'
        board[7][6] = 'W_Kn'

        #Placing the Bishops

        board[0][2] = 'B_B'
        board[0][5] = 'B_B'
        board[7][2] = 'W_B'
        board[7][5] = 'W_B'

        #Placing the Queens
        board[0][3] = 'B_Q'
        board[7][3] = 'W_Q'

        #Placing the Kings
        board[0][4] = 'B_K'
        board[7][4] = 'W_K'

        #Placing the Pawns

        for i in range(8):
            board[1][i] = 'B_P'
            board[6][i] = 'W_P'

        return board


#For Testing
if __name__ == '__main__':
    chess_board = Board()

    #Moving pawn two spaces
    #chess_board.move((6,0), (4,0))

    #print(repr(chess_board))
