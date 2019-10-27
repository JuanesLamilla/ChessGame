import pygame
from board import *

def draw_board(screen: pygame.Surface, width: int, animation:bool =False):
    """
    Draws the chess board on the given screen, according to the given width.
    """
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
    pygame.display.update()

def draw_pieces(screen: pygame.Surface, width: int, board: Board,
                animation:bool =False):
    """
    Draws the pieces on the given screen, according to the current status
    of the given board.
    """
    grid_width = width / 8
    for row in range(8):
        for col in range(8):
            if board.board[row][col]:
                x = grid_width * col
                y = grid_width * row
                if board.board[row][col] == 'B_R':
                    piece_image = pygame.image.load("PiecesPNG/BRook.png")
                elif board.board[row][col] == 'W_R':
                    piece_image = pygame.image.load("PiecesPNG/WRook.png")
                elif board.board[row][col] == 'B_Kn':
                    piece_image = pygame.image.load("PiecesPNG/BKnight.png")
                elif board.board[row][col] == 'W_Kn':
                    piece_image = pygame.image.load("PiecesPNG/WKnight.png")
                elif board.board[row][col] == 'B_B':
                    piece_image = pygame.image.load("PiecesPNG/BBishop.png")
                elif board.board[row][col] == 'W_B':
                    piece_image = pygame.image.load("PiecesPNG/WBishop.png")
                elif board.board[row][col] == 'B_Q':
                    piece_image = pygame.image.load("PiecesPNG/BQueen.png")
                elif board.board[row][col] == 'W_Q':
                    piece_image = pygame.image.load("PiecesPNG/WQueen.png")
                elif board.board[row][col] == 'B_K':
                    piece_image = pygame.image.load("PiecesPNG/BKing.png")
                elif board.board[row][col] == 'W_K':
                    piece_image = pygame.image.load("PiecesPNG/WKing.png")
                elif board.board[row][col] == 'B_P':
                    piece_image = pygame.image.load("PiecesPNG/BPawn.png")
                elif board.board[row][col] == 'W_P':
                    piece_image = pygame.image.load("PiecesPNG/WPawn.png")
                    
                screen.blit(piece_image, (x-5, y-5))
            if animation and row == 3:
                pygame.time.delay(50)
                pygame.display.update()
    pygame.time.delay(50)
    pygame.display.update()
                
                
def main():
    pygame.init()
    pygame.display.set_caption("Chess")
    width = 400
    screen = pygame.display.set_mode((width,width))
    screen.fill(pygame.Color(255,255,255))
    animation = True
    draw_board(screen, width, animation)
    board = Board()
    draw_pieces(screen, width, board, animation)
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
    pygame.display.quit()
    pygame.quit()
     
if __name__=="__main__":
    main()
    
