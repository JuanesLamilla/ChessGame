import pygame
from board import *

pygame.init()

width = 400
black = (0, 0, 0)
grey = (100, 100, 100)
white = (255, 255, 255)

pygame.display.set_caption("Chess")
screen = pygame.display.set_mode((width, width))


def draw_board(screen: pygame.Surface, width: int, animation:bool =False):
    """
    Draws the chess board on the given screen, according to the given width.
    """
    screen.fill(pygame.Color(255,255,255))
    y = 0
    grid_width = width / 8
    for row in range (8):
        if row % 2 == 0:
            x = width / 8
        else:
            x = 0
        for col in range (4):
            pygame.draw.rect(screen, pygame.Color(119,136,153),
                             pygame.Rect(x,y,grid_width,grid_width))
            if animation:
                pygame.time.delay(25)
                pygame.display.update()
            x = x + 2 * grid_width
        y = y + grid_width


def draw_pieces(screen: pygame.Surface, width: int, board: Board,
                animation:bool =False):
    """
    Draws the pieces on the given screen, according to the current status
    of the given board.
    """
    grid_width = width / 8
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
                screen.blit(piece_image, (x-5, y-5))
            if animation and row == 3:
                pygame.time.delay(50)
                pygame.display.update()


def button(msg, x, y, w, h, inactive_colour, active_colour, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(screen, inactive_colour, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(screen, active_colour, (x, y, w, h))

    small_text = pygame.font.Font("freesansbold.ttf", 30)
    text_surf = small_text.render(msg, True, white)
    text_rect = text_surf.get_rect()
    text_rect.center = ((x + (w / 2)), (y + (h / 2)))
    screen.blit(text_surf, text_rect)


def settings():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False

        screen.fill(white)
        large_text = pygame.font.Font('freesansbold.ttf', 50)
        text_surf = large_text.render("404 :(", True, black)
        text_rect = text_surf.get_rect()
        text_rect.center = ((width/2), (width/2) - 50)
        screen.blit(text_surf, text_rect)

        button("BACK", 125, 230, 175, 50, grey, black, intro_screen)

        pygame.display.update()
    pygame.display.quit()
    pygame.quit()


def intro_screen():

    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                intro = False

        piece_image = pygame.image.load("PiecesPNG/BRook.png")
        pygame.display.set_icon(piece_image)

        screen.fill(white)
        large_text = pygame.font.Font('freesansbold.ttf', 115)
        text_surf = large_text.render("Chess", True, black)
        text_rect = text_surf.get_rect()
        text_rect.center = ((width/2), (width/2) - 50)
        screen.blit(text_surf, text_rect)

        button("START", 125, 230, 175, 50, grey, black, main)
        button("SETTINGS", 125, 300, 175, 50, grey, black, settings)

        pygame.display.update()
    pygame.display.quit()
    pygame.quit()


def main():
    grid_width = width / 8
    board = Board()
    animation = False
    draw_board(screen, width, animation)
    draw_pieces(screen, width, board, animation)
    pygame.display.update()
    valid_moves = []
    if animation:
        logo = pygame.image.load("logo.png")
        screen.blit(logo, (0,1))
        pygame.time.delay(400)
        pygame.display.update()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x = int(event.pos[0] // grid_width)
                y = int(event.pos[1] // grid_width)
                draw_board(screen, width, False)
                selected = board.board[y][x]

                # select piece
                if selected != 0 and selected.colour == board.cur_turn:
                    pygame.draw.rect(screen, pygame.Color(78, 222, 188),
                             pygame.Rect(x * grid_width,y * grid_width,
                                         grid_width,grid_width))
                    valid_moves = board.get_valid_moves((y,x))
                    selected_coord = (y,x)
                    if valid_moves:
                        for move in valid_moves:
                            pygame.draw.rect(screen, pygame.Color(78, 222, 188),
                                 pygame.Rect(move[1] * grid_width + 3,move[0] *
                                             grid_width + 3, grid_width - 6,grid_width - 6))

                # show red square when user clicks on the opponent's piece
                elif selected != 0 and selected.colour != board.cur_turn:
                    pygame.draw.rect(screen, pygame.Color(255, 0, 0),
                             pygame.Rect(x * grid_width,y * grid_width,
                                         grid_width,grid_width))
                    draw_pieces(screen, width, board, False)
                    pygame.display.update()
                    pygame.time.delay(100)
                    draw_board(screen, width, False)
                
                # move selected piece
                elif selected == 0 and valid_moves and (y,x) in valid_moves:
                    board.move (selected_coord, (y,x))

                draw_pieces(screen, width, board, False)
                pygame.display.update()

    pygame.display.quit()
    pygame.quit()


if __name__ == "__main__":
    intro_screen()
