from csc290 import board
from csc290 import player
from csc290 import GUI


class Game:
    """
    The game class where the state of the game is checked, and players turns are
    started and switched after each turn. Acts as a main by controlling the flow
    of the game and ending the game when necessary.

    """

    def __init__(self):
        """
        initializes the game class with a board and game_status set to False
        """
        self.game_status = False
        self.board = board.Board()
        self.players = []

    def set_players(self, name1: str, name2: str) -> None:
        """
        creates 2 player objects each with a  given name
        the colour of player1 and 2 will be white and black respectively,
        then adds them to the players attribute.

        >>> self.set_players("Bob", "Jeff")
        >>> self.players[0].name
        "Bob"
        >>> self.players[1].name
        "Jeff"
        >>> self.players[0].colour
        "W"
        >>> self.players[1].colour
        "B"
        """
        player1 = player.Player(name1)
        player2 = player.Player(name2)
        player2.set_colour("B")
        self.players.append(player1, player2)

    def start_game(self) -> None:
        """
        creates the gui, sets game_status to True
        and starts the first players turn.
        """
        self.game_status = True
        GUI.main()
        self.player_turn(self.players[0])

    def update_game_status(self) -> None:
        """
        updates the game_status attribute to True if and only if the game is
        still in progress, if the game has ended sets to False instead.
        """
        #checks the length of the list returned by has_move
        #since if only 1 player has a move then the game should be ended
        #TODO update this logic to check if the current player has a move
        if len(self.has_move()) == 1:
            self.game_status = False
        else:
            self.game_status = True

    def has_move(self) -> list:
        """
        returns a list containing "W" if white has a move anywhere on the board, "B" if black
        has a turn anywhere on the board, and "N" if neither player has a move
        anywhere on the board. This is regardless of whose turn it is.
        """
        #TODO implement has_move() w.r.t get_valid_moves from board class
        pass

    def player_turn(self, player: Player) -> None:
        """
        calls the move method from the board class for the player whose turn it
        currently is, then updates cur_turn to hold the other player.
        """
        #TODO implement a players turn so that on their turn the player can move
        #one of their pieces

        self.update_game_status()
        if not self.game_status:
            self.end_game()
        elif board.Board.cur_turn == "W":
            board.Board.cur_turn = "B"
        else:
            board.Board.cur_turn == "W"

    def end_game(self):
        """
        if the game_status attribute is False, end the game by resetting the board.
        """
        if not self.game_status:
            self.board = board.Board()


if __name__ == "__main__":
    game = Game()
    name1 = input("Please enter the name of player1 (White)")
    name2 = input("Please enter the name of player2 (Black)")
    game.set_players(name1, name2)
    game.start_game()
