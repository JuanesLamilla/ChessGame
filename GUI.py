import pygame
from board import *

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
                
                
def main():
    pygame.init()
    pygame.display.set_caption("Chess")
    width = 400
    grid_width = width / 8
    board = Board()
    animation = True
    screen = pygame.display.set_mode((width,width))
    draw_board(screen, width, animation)
    draw_pieces(screen, width, board, animation)
    pygame.display.update()
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
                if board.board[y][x] != 0:
                    pygame.draw.rect(screen, pygame.Color(78, 222, 188),
                             pygame.Rect(x * grid_width,y * grid_width,
                                         grid_width,grid_width))
                draw_pieces(screen, width, board, False)
                pygame.display.update()
                
                
    pygame.display.quit()
    pygame.quit()
     
if __name__=="__main__":
    main()
    
