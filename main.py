import pygame


width = 600
height = 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
CUSTWHITE = (3, 252, 215)
CUSTBLACK = (252, 198, 3)
SQUARESIZE = 75

pawn = 1
knight = 3
bishop = 4
rook = 5
queen = 9
king = 10
empty = 0

board = [[-rook, -knight, -bishop, -queen, -king, -bishop, -knight, -rook],
         [-pawn, -pawn, -pawn, -pawn, -pawn, -pawn, -pawn, -pawn],
         [empty, empty, empty, empty, empty, empty, empty, empty],
         [empty, empty, empty, empty, empty, empty, empty, empty],
         [empty, empty, empty, empty, empty, empty, empty, empty],
         [empty, empty, empty, empty, empty, empty, empty, empty],
         [pawn, pawn, pawn, pawn, pawn, pawn, pawn, pawn],
         [rook, knight, bishop, queen, king, bishop, knight, rook]]


def main():
    pygame.init()
    display = pygame.display.set_mode((width, height))
    clock = pygame.time.Clock()

    crashed = False

    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True
            drawboard(display)
        print(event)
        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()


def drawboard(display):
    for row in range(0, 8):
        for col in range(0, 8):
            startrow = col * SQUARESIZE
            startcol = row * SQUARESIZE

            pygame.draw.rect(display, CUSTWHITE if (row + col) % 2 == 0 else CUSTBLACK,
                             [startrow, startcol, SQUARESIZE, SQUARESIZE])


            piece = getimage(board[row][col])
            if piece is not None:
                piecewidth = (startrow + SQUARESIZE / 2) - piece.get_width() / 2
                pieceheight = (startcol + SQUARESIZE / 2) - piece.get_height() / 2
                display.blit(piece, (piecewidth, pieceheight))


def getimage(piece):
    if piece == -rook:
        return pygame.image.load('rook_black.png')
    if piece == -knight:
        return pygame.image.load('knight_black.png')
    if piece == -bishop:
        return pygame.image.load('bishop_black.png')
    if piece == -queen:
        return pygame.image.load('queen_black.png')
    if piece == -king:
        return pygame.image.load('king_black.png')
    if piece == -pawn:
        return pygame.image.load('pawn_black.png')

    if piece == rook:
        return pygame.image.load('rook_white.png')
    if piece == knight:
        return pygame.image.load('knight_white.png')
    if piece == bishop:
        return pygame.image.load('bishop_white.png')
    if piece == queen:
        return pygame.image.load('queen_white.png')
    if piece == king:
        return pygame.image.load('king_white.png')
    if piece == pawn:
        return pygame.image.load('pawn_white.png')


if __name__ == '__main__':
    main()