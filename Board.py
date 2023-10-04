# The Board class is an essential part of the X-O game. 
# It represents the game board and provides methods to update and check its state. 

class Board:
    # The __init__ method initializes a new board with a user-defined size greater than 2.
    def __init__(self):
        while True:
            self.size = int(input("what is the board size you want to play on that greater than 2: "))
            if self.size>2:
                break
        self.board = [[' ']*self.size for _ in range(self.size)]

    # The PrintBoard method prints the current state of the board, making it easy for players to visualize their moves.
    def PrintBoard(self):
        print()
        for i in range(self.size):
            for j in range(self.size):
                print('',self.board[i][j],end=' ')
                if j !=self.size-1:
                    print('|',end = '')
                else:
                    print()
            if i !=self.size-1:
                print("---"*self.size+"-"*(self.size-1))
            else:
                print()

    # The UpdateBoard method updates the board with a new move, ensuring that it is valid and not already occupied.
    def UpdateBoard(self,X,Y,symbol):
        if (X not in range(self.size)) or (Y not in range(self.size)) or self.board[X][Y]!=' ':
            return False
        self.board[X][Y] = symbol
        return True
    
    # The isWinner method checks if a player has won the game by checking all rows, columns, and diagonals for matching symbols.
    def isWinner(self,symbol):
        for row in self.board:
            if row.count(symbol)==self.size:
                return True
        for indexcols in range(self.size):
            col = [row[indexcols] for row in self.board]
            if col.count(symbol)==self.size:
                return True
        diagonal = [[self.board[index][index] for index in range(self.size)],
                    [self.board[index][self.size-index-1] for index in range(self.size)]]
        if diagonal[0].count(symbol) == self.size or diagonal[1].count(symbol) == self.size:
            return True
        return False
    
    # the isDraw method checks if the game has ended in a draw by checking if all cells are occupied but no player has won.
    def isDraw(self):
        plays = 0
        for row in self.board:
            plays += row.count(' ')
        if plays == 0:
            return True
        return False

