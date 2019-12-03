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

        coord_piece = self.return_valid_piece(coordinate)

        if isinstance(coord_piece, pieces.Pawn):
            return self.get_pawn_moves(coordinate)

        if isinstance(coord_piece, pieces.Knight):
            return self.get_knight_moves(coordinate)

        if isinstance(coord_piece, pieces.Rook):
            return self.get_rook_moves(coordinate)

        if isinstance(coord_piece, pieces.Bishop):
            return self.get_bishop_moves(coordinate)

        if isinstance(coord_piece, pieces.Queen):
            return self.get_queen_moves(coordinate)

        if isinstance(coord_piece, pieces.King):
            return self.basic_king_moves(coordinate)


    def get_pawn_moves(self, coordinate):
        """
        Returns a list of valid moves for the pawn piece at a given coordinate.
        """

        cur_x = coordinate[0]
        cur_y = coordinate[1]
        cur_pawn = self.board[cur_x][cur_y]

        valid_moves = []

        #if player Black
        if self.cur_turn == 'B':

            #case for pawn's first move
            if cur_pawn._start:
                for i in range(cur_x + 1, cur_x + 3):
                    potential_coord = (i, cur_y)

                    if not self.is_blocked(potential_coord, True) and self.is_boundary(potential_coord):
                        valid_moves.append(potential_coord)

            #case for pawn's 2nd move and beyond
            else:
                potential_coord = (cur_x+1, cur_y)

                if not self.is_blocked(potential_coord, True) and self.is_boundary(potential_coord):
                    valid_moves.append(potential_coord)

            #if there is a black piece located diagnoally:

            if self.is_boundary((cur_x+1, cur_y +1)):
                potential_piece = self.return_valid_piece((cur_x+1, cur_y+1))
                if potential_piece != 0 and potential_piece.colour != self.cur_turn:
                    valid_moves.append((cur_x+1, cur_y+1))

            if self.is_boundary((cur_x+1, cur_y -1)):
                potential_piece = self.return_valid_piece((cur_x+1, cur_y-1))
                if potential_piece != 0 and potential_piece.colour != self.cur_turn:
                    valid_moves.append((cur_x+1, cur_y-1))

        #if player white

        else:

            #case for pawn's first move
            if cur_pawn._start:
                for i in range(cur_x -2, cur_x):
                    potential_coord = (i, cur_y)

                    if not self.is_blocked(potential_coord, True) and self.is_boundary(potential_coord):
                        valid_moves.append(potential_coord)

            #case for pawn's 2nd move and beyond
            else:
                potential_coord = (cur_x-1, cur_y)

                if not self.is_blocked(potential_coord, True) and self.is_boundary(potential_coord):
                    valid_moves.append(potential_coord)

            #if there is a black piece located diagnoally:

            if self.is_boundary((cur_x-1, cur_y -1)):
                potential_piece = self.return_valid_piece((cur_x-1, cur_y-1))
                if potential_piece != 0 and potential_piece.colour != self.cur_turn:
                    valid_moves.append((cur_x-1, cur_y-1))

            if self.is_boundary((cur_x-1, cur_y +1)):
                potential_piece = self.return_valid_piece((cur_x-1, cur_y+1))
                if potential_piece != 0 and potential_piece.colour != self.cur_turn:
                    valid_moves.append((cur_x-1, cur_y+1))

        return valid_moves

    def get_knight_moves(self, coordinate):
        """
        Returns a list of valid moves for the knight piece at a given coordinate.
        """

        cur_x = coordinate[0]
        cur_y = coordinate[1]

        valid_moves = []

        #fwd left cases
        if self.is_boundary((cur_x-2, cur_y-1)) and not self.is_blocked((cur_x-2, cur_y-1), False):
            valid_moves.append((cur_x-2, cur_y-1))

        if self.is_boundary((cur_x-1, cur_y-2)) and not self.is_blocked((cur_x-1, cur_y-2), False):
            valid_moves.append((cur_x-1, cur_y-2))

        #fwd right cases
        if self.is_boundary((cur_x-2, cur_y+1)) and not self.is_blocked((cur_x-2, cur_y+1), False):
            valid_moves.append((cur_x-2, cur_y+1))

        if self.is_boundary((cur_x-1, cur_y+2)) and not self.is_blocked((cur_x-1, cur_y+2), False):
            valid_moves.append((cur_x-1, cur_y+2))

        #bwrd left cases
        if self.is_boundary((cur_x+2, cur_y-1)) and not self.is_blocked((cur_x+2, cur_y-1), False):
            valid_moves.append((cur_x+2, cur_y-1))

        if self.is_boundary((cur_x+1, cur_y-2)) and not self.is_blocked((cur_x+1, cur_y-2), False):
            valid_moves.append((cur_x+1, cur_y-2))

        #bwrd right cases
        if self.is_boundary((cur_x+2, cur_y+1)) and not self.is_blocked((cur_x+2, cur_y+1), False):
            valid_moves.append((cur_x+2, cur_y+1))

        if self.is_boundary((cur_x+1, cur_y+2)) and not self.is_blocked((cur_x+1, cur_y+2), False):
            valid_moves.append((cur_x+1, cur_y+2))

        return valid_moves


    def get_rook_moves(self, coordinate):
        """
        Returns a list of valid moves for the rook piece at a given coordinate.
        """

        cur_x = coordinate[0]
        cur_y = coordinate[1]

        valid_moves = []

        #x-axis movement

        if self.cur_turn == 'B':

            for i in range(0, cur_x):

                if self.is_blocked((i, cur_y), False):
                    break

                else:
                    valid_moves.append((i, cur_y))

                    if isinstance(self.board[i][cur_y], pieces.Piece):
                        break

            for i in range(cur_x+1, 8):

                if self.is_blocked((i, cur_y), False):
                    break

                else:
                    valid_moves.append((i, cur_y))

                    if isinstance(self.board[i][cur_y], pieces.Piece):
                        break

        else:

            for i in range(cur_x-1, -1 , -1):

                if self.is_blocked((i, cur_y), False):
                    break

                else:
                    valid_moves.append((i, cur_y))

                    if isinstance(self.board[i][cur_y], pieces.Piece):
                        break

            for i in range(cur_x+1, 8):

                if self.is_blocked((i, cur_y), False):
                    break

                else:
                    valid_moves.append((i, cur_y))

                    if isinstance(self.board[i][cur_y], pieces.Piece):
                        break

        #y-axis movement

        for j in range(0, cur_y):

            if self.is_blocked((cur_x, j), False):
                break

            else:
                valid_moves.append((cur_x, j))

                if isinstance(self.board[cur_x][j], pieces.Piece):
                    break

        for j in range(cur_y+1, 8):

            if self.is_blocked((cur_x, j), False):
                break

            else:
                valid_moves.append((cur_x, j))

                if isinstance(self.board[cur_x][j], pieces.Piece):
                    break

        return valid_moves

    def get_bishop_moves(self, coordinate):
        """
        Returns a list of valid moves for the bishop piece at a given coordinate.
        """

        cur_x = coordinate[0]
        cur_y = coordinate[1]
        valid_moves = []

        #top left movement
        top_left_movement = (-1, -1)
        potential_coord = tuple(map(sum, zip(coordinate, top_left_movement)))

        while self.is_boundary(potential_coord) and not self.is_blocked(potential_coord, False):
            valid_moves.append(potential_coord)
            if isinstance(self.board[potential_coord[0]][potential_coord[1]], pieces.Piece):
                break
            potential_coord = tuple(map(sum, zip(potential_coord, top_left_movement)))


        #top right movement
        top_right_movement = (1, 1)
        potential_coord = tuple(map(sum, zip(coordinate, top_right_movement)))

        while self.is_boundary(potential_coord) and not self.is_blocked(potential_coord, False):
            valid_moves.append(potential_coord)
            if isinstance(self.board[potential_coord[0]][potential_coord[1]], pieces.Piece):
                break
            potential_coord = tuple(map(sum, zip(potential_coord, top_right_movement)))

        #bottom left movement
        bot_left_movement = (1, -1)
        potential_coord = tuple(map(sum, zip(coordinate, bot_left_movement)))

        while self.is_boundary(potential_coord) and not self.is_blocked(potential_coord, False):
            valid_moves.append(potential_coord)
            if isinstance(self.board[potential_coord[0]][potential_coord[1]], pieces.Piece):
                break
            potential_coord = tuple(map(sum, zip(potential_coord, bot_left_movement)))

        #bottom right movement
        bot_right_movement = (-1, 1)
        potential_coord = tuple(map(sum, zip(coordinate, bot_right_movement)))

        while self.is_boundary(potential_coord) and not self.is_blocked(potential_coord, False):
            valid_moves.append(potential_coord)
            if isinstance(self.board[potential_coord[0]][potential_coord[1]], pieces.Piece):
                break
            potential_coord = tuple(map(sum, zip(potential_coord, bot_right_movement)))

        return valid_moves

    def get_queen_moves(self, coordinate):
        """
        Returns a list of valid moves for the queen piece at a given coordinate
        """

        bishop_moves = self.get_bishop_moves(coordinate)
        rook_moves = self.get_rook_moves(coordinate)

        valid_moves = bishop_moves + rook_moves

        return valid_moves

    def basic_king_moves(self, coordinate):
        """
        Returns the basic movement of King - not including Check positions
        """
        cur_x = coordinate[0]
        cur_y = coordinate[1]
        valid_moves = []

        #Left/right side movement
        for i in range(-1, 2):
            potential_coord_left = (cur_x+i, cur_y - 1)
            potential_coord_right = (cur_x+i, cur_y + 1)

            if i != 0:
                potential_coord_center = (cur_x+i, cur_y)
                if self.is_boundary(potential_coord_center) and not self.is_blocked(potential_coord_center, False):
                    valid_moves.append(potential_coord_center)

            if self.is_boundary(potential_coord_left) and not self.is_blocked(potential_coord_left, False):
                valid_moves.append(potential_coord_left)

            if self.is_boundary(potential_coord_right) and not self.is_blocked(potential_coord_right, False):
                valid_moves.append(potential_coord_right)

        return valid_moves

    def get_king_moves(self, coordinate):
        """
        Returns a list of valid moves for the King piece at a given coordinate
        """
        if self.cur_turn == 'W':
            opp_moves = self.get_all_moves()['B']

        else:
            opp_moves = self.get_all_moves()['W']

        king_movement = self.get_king_moves(coordinate)

        valid_moves = [x for x in king_movement if x not in opp_moves]

        return valid_moves

    def get_all_moves(self):
        """
        Returns a dictionary of all moves.
        Keys are the player and the values are the moves themselves.
        """
        white_moves = []
        black_moves = []

        for i in range(8):
            for j in range(8):

                if isinstance(self.return_valid_piece((i,j)), pieces.Piece):

                    piece = self.board[i][j]
                    coord = (i, j)

                    if piece.colour == 'W':
                        white_moves.append(self.get_valid_moves(coord))

                    else:
                        black_moves.append(self.get_valid_moves(coord))

        return {'B': black_moves, 'W': white_moves}

    def is_blocked(self, coordinate, is_pawn):
        """
        Check to see if piece at coordinate is a potential blocking move.
        """
        cur_x = coordinate[0]
        cur_y = coordinate[1]

        piece = self.board[cur_x][cur_y]
        #print ("block_check")
        #If nothing at coordinate, then it's a safe move.
        if piece == 0:
            return False

        else:

            #action passed if its a pawn - it can't attack straight on.
            if is_pawn:
                return True

            elif piece.colour == self.cur_turn:
                return True

        return False

    def is_boundary(self, coordinate):
        """
        Checks to see if coordinate is in boundary of the board
        """
        cur_x = coordinate[0]
        cur_y = coordinate[1]

        if cur_x < 0 or cur_x > 7 or cur_y < 0 or cur_y > 7:
            return False

        else:
            return True


    def return_valid_piece(self, coordinate):
        """
        Returns a piece at the coordinate - if it exists.
        Returns 0 otherwise
        """

        cur_x = coordinate[0]
        cur_y = coordinate[1]

        #if coordinate contains a piece
        if self.board[cur_x][cur_y] != 0:
            return self.board[cur_x][cur_y]

        else:
            return 0


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

        if isinstance(self.board[new_x][new_y], pieces.Pawn):
            self.board[new_x][new_y].made_first_move()

        if self.cur_turn == 'B':
            self.cur_turn = 'W'

        else:
            self.cur_turn = 'B'

    def can_capture(self, old_cord, new_cord):
        """
        called by move and gui to check if the tile that the player is tying
        to move to is occupied by an opponents piece that can be captured.
        """
        old_x = old_cord[0]
        old_y = old_cord[1]
        new_x = new_cord[0]
        new_y = new_cord[1]
        if self.return_valid_piece(old_cord) == 0:
            return False
        if self.return_valid_piece(old_cord).colour != \
                self.return_valid_piece(new_cord).colour \
                and new_cord in self.get_valid_moves(old_cord):
            return True
        return False

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
        board[7][6] = pieces.Knight('W')

        #Placing the Bishops

        board[0][2] = pieces.Bishop('B')
        board[0][5] = pieces.Bishop('B')
        board[7][2] = pieces.Bishop('W')
        board[7][5] = pieces.Bishop('W')

        #Placing the Queens
        board[0][3] = pieces.Queen('B')
        board[7][3] = pieces.Queen('W')

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
    ''' Knight Test
    chess_board.cur_turn = 'B'
    chess_board.move((0,1), (3,3))
    print(chess_board.get_valid_moves((3,3)))
    '''


    #Rook Test
    '''
    chess_board.cur_turn = 'B'
    chess_board.move((1,0), (7,7))
    chess_board.move((0,0), (2,0))
    '''
    '''
    chess_board.move((6,7), (0,0))
    chess_board.move((7,7), (3,3))
    print(chess_board.get_valid_moves((3,3)))
    '''

    '''
    #Bishop Test
    chess_board.move((7,5), (4,3))
    print(chess_board.board[4][3])
    print(chess_board.get_valid_moves((4,3)))
    '''

    #Moving black pieces to vulnerable positions to be attacked by white pawn
    #chess_board.move((1,2), (5,2))
    #chess_board.move((1,3), (5,0))

    #get the valid move for pawn located at (6,1)
    #print(chess_board.get_valid_moves((6,1)))

    #check case when pawn has already moved
    #chess_board.move((6,1), (4,1))
    #print(chess_board.get_valid_moves((4,1)))

    #Testing black's Pawn
    #chess_board.cur_turn = 'B'

    #Moving white spaces to vulnerable positions to be attacked by black pawn
    #chess_board.move((6,1), (2,2))
    #chess_board.move((6,0), (2,0))

    #get the valid move for pawn located at (6,1)
    #print(chess_board.get_valid_moves((1,2)))

    #print(chess_board.get_valid_moves((1,1)))
    #chess_board.move((1,2), (2,2))


    #print(repr(chess_board))
