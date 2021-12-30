
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
    while True:
        row = int(input('row'))
        col = int(input('col'))
        print(board[row][col])

if __name__ == '__main__':
    main()
