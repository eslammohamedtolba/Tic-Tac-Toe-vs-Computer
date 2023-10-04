# This class represents a player in the X-O game.
# The __init__ method initializes a new player with a name and symbol.
# The play method prompts the user to enter their move and returns it as a list of coordinates.

class Player:
    def __init__(self):
        self.Name = input("what is your name: ")
        while True:
            self.Symbol = input("please enter your symbol from following symbols X or O: ")
            if self.Symbol in ['X','O']:
                break
    def play(self,board):
        x = int(input("please enter x number: "))
        y = int(input("please enter y number: "))
        return [x,y]





# This class represents a computer player in the X-O game 
# It uses backtracking and minmax algorithms to find the best move.

class ComputerPlayer:
    # The __init__ method initializes a new player with a name and symbol based on the other player symbol
    def __init__(self,symbolPlayer):
        self.Name = "computer Player"
        self.Symbol = "O" if symbolPlayer=="X" else "X"
    
    # The state method checks the current state of the game if winning or draw or still the game is running 
    def state(self,board,IsComputer,symbol):
        if board.isWinner(symbol):
            if IsComputer:
                # winning for computer player
                return 1
            else:
                # losing for computer player
                return -1
            
        elif board.isDraw():
            # drawing for both players
            return 0
        else:
            # still game continuing 
            return -2
        
    # The ChooseSuit method chooses the best move for the computer player by backtracking and minmax algorithms
    def ChooseSuit(self,board,IsComputer):
        playing=[0,0,-2 if IsComputer else 2]
        for X in range(board.size):
            for Y in range(board.size):
                if board.UpdateBoard(X,Y,self.Symbol if IsComputer else ('O' if self.Symbol=='X' else 'X')):
                    currentstate = self.state(board,IsComputer,self.Symbol if IsComputer else ('O' if self.Symbol=='X' else 'X'))
                    if currentstate==-2:
                        againstPlaying = self.ChooseSuit(board,0 if IsComputer==1 else 1)
                        if IsComputer==1:
                            if againstPlaying[2]>playing[2]:
                                playing=[X,Y,againstPlaying[2]]
                        else:
                            if againstPlaying[2]<playing[2]:
                                playing=[X,Y,againstPlaying[2]]
                    else:
                        if IsComputer==1:
                            if currentstate>playing[2]:
                                playing=[X,Y,currentstate]
                        else:
                            if currentstate<playing[2]:
                                playing=[X,Y,currentstate]
                    board.board[X][Y]=' '
        return playing

    def play(self,board):
        X,Y= self.ChooseSuit(board,1)[:2]
        return [X,Y]






