
from Player import *
from Board import *

# The `Game` class is a well-structured and organized implementation of a two-player board game.
class Game:
    # The `__init__` method initializes the `board`, `Players`, and `GameRunning` attributes of the `Game` class.
    def __init__(self):
        self.board = Board()
        self.Players = []
        self.GameRunning=True

    # The `if-elif` block in the `StartGame` method allows players to choose whether they want to play with another player or with a computer.
    def StartGame(self):
        self.Players.append(Player())
        while True:
            typeSplayer = int(input("Do you want to play with another player(0) or with computer(1): "))
            if typeSplayer == 0:
                self.Players.append(Player())
                break
            elif typeSplayer == 1:
                self.Players.append(ComputerPlayer(self.Players[0].Symbol))
                break

        self.board.PrintBoard()
        while self.GameRunning:
            for player in self.Players:
                while True:
                    # The nested `if-elif` block in the same loop checks if there is a winner or if it's a draw and ends the game accordingly.
                    if type(player)==Player:
                        print(f"please {player.Name} with symbol {player.Symbol} enter indices between 0 and {self.board.size-1} in empty places")
                    playing = player.play(self.board)
                    if self.board.UpdateBoard(playing[0],playing[1],player.Symbol):
                        break
                if type(player)==ComputerPlayer:
                    print("the computer player played on ({},{})".format(playing[0],playing[1]))

                self.board.PrintBoard()
                if self.board.isWinner(player.Symbol):
                    print("the player {} won!".format(player.Name))
                    self.GameRunning=False
                    break
                elif self.board.isDraw():
                    print("it's draw")
                    self.GameRunning=False
                    break