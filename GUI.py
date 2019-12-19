import pygame
from board import *


class GUI:
    """
    represents the gui of the game.
    """
    def __init__(self):
        """
        initializer for the Gui class
        """
        pygame.init()
        pygame.font.init()

        self.width = 400
        self.black = (0, 0, 0)
        self.grey = (100, 100, 100)
        self.white = (255, 255, 255)

        pygame.display.set_caption("Chess")
        self.screen = pygame.display.set_mode((self.width, self.width))

        self.timer = False


    def draw_board(self, animation:bool =False):
        """
        Draws the chess board on the given screen, according to the given width.
        """
        self.screen.fill(pygame.Color(255, 255, 255), (0,0,self.width,self.width))
        y = 0
        grid_width = self.width / 8
        for row in range(8):
            if row % 2 == 0:
                x = self.width / 8
            else:
                x = 0
            for col in range(4):
                pygame.draw.rect(self.screen, pygame.Color(119, 136, 153),
                                     pygame.Rect(x, y, grid_width, grid_width))
                if animation:
                    pygame.time.delay(25)
                    pygame.display.update()
                x = x + 2 * grid_width
            y = y + grid_width

    def draw_pieces(self, board: Board, animation:bool =False):
        """
        Draws the pieces on the given screen, according to the current status
        of the given board.
        """
        grid_width = self.width / 8
        for row in range(8):
            for col in range(8):
                if board.board[row][col] != 0:
                    x = grid_width * col
                    y = grid_width * row
                    if board.board[row][col].__class__.__name__ == 'Rook':
                        if board.board[row][col].colour == 'B':
                            piece_image = pygame.image.load("PiecesPNG/BRook.png")
                        else:
                            piece_image = pygame.image.load("PiecesPNG/WRook.png")
                    elif board.board[row][col].__class__.__name__ == 'Knight':
                        if board.board[row][col].colour == 'B':
                            piece_image = pygame.image.load("PiecesPNG/BKnight.png")
                        else:
                            piece_image = pygame.image.load("PiecesPNG/WKnight.png")
                    elif board.board[row][col].__class__.__name__ == 'Bishop':
                        if board.board[row][col].colour == 'B':
                            piece_image = pygame.image.load("PiecesPNG/BBishop.png")
                        else:
                            piece_image = pygame.image.load("PiecesPNG/WBishop.png")
                    elif board.board[row][col].__class__.__name__ == 'Queen':
                        if board.board[row][col].colour == 'B':
                            piece_image = pygame.image.load("PiecesPNG/BQueen.png")
                        else:
                            piece_image = pygame.image.load("PiecesPNG/WQueen.png")
                    elif board.board[row][col].__class__.__name__ == 'King':
                        if board.board[row][col].colour == 'B':
                            piece_image = pygame.image.load("PiecesPNG/BKing.png")
                        else:
                            piece_image = pygame.image.load("PiecesPNG/WKing.png")
                    elif board.board[row][col].__class__.__name__ == 'Pawn':
                        if board.board[row][col].colour == 'B':
                            piece_image = pygame.image.load("PiecesPNG/BPawn.png")
                        else:
                            piece_image = pygame.image.load("PiecesPNG/WPawn.png")
                    self.screen.blit(piece_image, (x-5, y-5))
                if animation and row == 3:
                    pygame.time.delay(50)
                    pygame.display.update()

    def button(self, msg, x, y, w, h, inactive_colour, active_colour, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(self.screen, inactive_colour, (x, y, w, h))
            if click[0] == 1 and action is not None:
                action()
        else:
            pygame.draw.rect(self.screen, active_colour, (x, y, w, h))

        small_text = pygame.font.Font("freesansbold.ttf", 30)
        text_surf = small_text.render(msg, True, self.white)
        text_rect = text_surf.get_rect()
        text_rect.center = ((x + (w / 2)), (y + (h / 2)))
        self.screen.blit(text_surf, text_rect)


    def switch(self, msg, x, y):
        mouse = pygame.mouse.get_pos()

        click = pygame.mouse.get_pressed()

        pygame.draw.circle(self.screen, self.black, (x, y), 10, 3)

        if self.timer:
            pygame.draw.circle(self.screen, self.black, (x, y), 5)

        if x + 5 > mouse[0] > x - 5 and y + 5 > mouse[1] > y - 5 and click[0] == 1:
            if not self.timer:
                pygame.draw.circle(self.screen, self.black, (x, y), 5)
                self.timer = True
            else:
                self.timer = False

        small_text = pygame.font.Font('freesansbold.ttf', 25)
        text_surf2 = small_text.render(msg, True, self.black)
        text_rect2 = text_surf2.get_rect()
        text_rect2.center = (x + 60, 185)
        self.screen.blit(text_surf2, text_rect2)

    def settings(self):
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False

            self.screen.fill(self.white)
            large_text = pygame.font.Font('freesansbold.ttf', 50)
            text_surf = large_text.render("Settings", True, self.black)
            text_rect = text_surf.get_rect()
            text_rect.center = ((self.width/2), (self.width/2) - 75)
            self.screen.blit(text_surf, text_rect)

            self.switch("Timer", 140, 185)

            self.button("START", 125, 230, 175, 50, self.grey, self.black, self.main)

            pygame.display.update()
        pygame.display.quit()
        pygame.quit()

    def intro_screen(self):
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False

            piece_image = pygame.image.load("PiecesPNG/BRook.png")
            pygame.display.set_icon(piece_image)

            self.screen.fill(self.white)
            logo = pygame.image.load("logo.png")
            self.screen.blit(logo, (0,-70))

            self.button("START", 125, 230, 175, 50, self.grey, self.black, self.main)
            self.button("SETTINGS", 125, 300, 175, 50, self.grey, self.black, self.settings)

            pygame.display.update()
        pygame.display.quit()
        pygame.quit()

    def winner_screen(self, winner: str, msg: str):
        intro = True

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False

            piece_image = pygame.image.load("PiecesPNG/BRook.png")
            pygame.display.set_icon(piece_image)

            self.screen.fill(self.white)

            large_text = pygame.font.Font('freesansbold.ttf', 50)
            winner_text = "Player " + winner + " wins!"
            text_surf = large_text.render(winner_text, True, self.black)
            text_rect = text_surf.get_rect()
            text_rect.center = ((self.width / 2), (self.width / 2) - 50)
            self.screen.blit(text_surf, text_rect)

            large_text = pygame.font.Font('freesansbold.ttf', 20)
            text_surf = large_text.render(msg, True, self.black)
            text_rect = text_surf.get_rect()
            text_rect.center = ((self.width / 2), (self.width / 2) - 10)
            self.screen.blit(text_surf, text_rect)

            self.button("GO AGAIN", 125, 230, 175, 50, self.grey, self.black, self.main)
            self.button("SETTINGS", 125, 300, 175, 50, self.grey, self.black, self.settings)

            pygame.display.update()
        pygame.display.quit()
        pygame.quit()

    def main(self):
        grid_width = self.width / 8

        height = 455
        if self.timer:
            pygame.display.set_mode((self.width, height))
        else:
            pygame.display.set_mode((self.width, self.width))
        pygame.display.update()

        board = Board()
        animation = True
        self.draw_board(animation)
        self.draw_pieces(board, animation)
        pygame.display.update()
        valid_moves = []

        clock = pygame.time.Clock()
        time_one = 300
        time_two = 300

        pygame.time.set_timer(pygame.USEREVENT, 1000)

        running = True
        while running:
            for event in pygame.event.get():

                clock.tick()

                if self.timer:

                    if board.cur_turn == 'W' \
                            and event.type == pygame.USEREVENT:
                        time_one -= 1

                    elif board.cur_turn == 'B' \
                            and event.type == pygame.USEREVENT:
                        time_two -= 1

                    self.button(seconds_to_clock(time_one),
                                20, 405, 175, 50, self.black, self.black)
                    self.button(seconds_to_clock(time_two),
                                205, 405, 175, 50, self.black, self.black)

                    pygame.display.update()

                    if time_one == 0:
                        self.winner_screen("2", "Player 1 ran out of time.")
                    elif time_two == 0:
                        self.winner_screen("1", "Player 2 ran out of time.")

                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    x = int(event.pos[0] // grid_width)
                    y = int(event.pos[1] // grid_width)

                    if y >= 8:
                        break

                    self.draw_board(False)
                    selected = board.board[y][x]

                    # select piece
                    if selected != 0 and selected.colour == board.cur_turn:
                        pygame.draw.rect(self.screen, pygame.Color(78, 222, 188),
                                 pygame.Rect(x * grid_width, y * grid_width,
                                             grid_width, grid_width))
                        valid_moves = board.get_valid_moves((y, x))
                        selected_coord = (y, x)
                        if valid_moves:
                            for move in valid_moves:
                                pygame.draw.rect(self.screen, pygame.Color(78, 222, 188),
                                     pygame.Rect(move[1] * grid_width + 3,move[0] *
                                                 grid_width + 3, grid_width - 6, grid_width - 6))

                    # show red square when user clicks on the opponent's piece
                    elif selected != 0 and selected.colour != board.cur_turn\
                            and not board.can_capture(selected_coord, (y, x)):

                        pygame.draw.rect(self.screen, pygame.Color(255, 0, 0),
                                 pygame.Rect(x * grid_width,y * grid_width,
                                             grid_width,grid_width))
                        self.draw_pieces(board, False)
                        pygame.display.update()
                        pygame.time.delay(100)
                        self.draw_board(False)

                    # move selected piece
                    elif (selected == 0 or board.can_capture(selected_coord, (y,x)))\
                            and valid_moves and (y, x) in valid_moves:
                        board.move(selected_coord, (y, x))

                    self.draw_pieces(board, False)
                    pygame.display.update()

        pygame.display.quit()
        pygame.quit()


def seconds_to_clock(original: int) -> str:
    minutes = original // 60
    seconds = str(original % 60)
    if seconds == '0':
        seconds = '00'
    if len(seconds) == 1:
        seconds = "0" + seconds
    return str(minutes) + ":" + seconds


if __name__ == "__main__":
    gui = GUI()
    gui.intro_screen()
