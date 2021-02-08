from TableDisplay import DisplayTable
from GameData import GameData
from Shoe import Shoe

class PlayerInputState:
    def __init__(self):
        self.GameIsOver = False
        self.NextState = self

    def Update(self):
        DisplayTable(True, "(H)it, (S)tand, (Q)uit")
        response = input("> ")
        if(response == "h" or response == "H"):
            gameData = GameData.getInstance()
            shoe = Shoe.getInstance()
            gameData.AddPlayerCard(shoe.DrawRandom())
            from EvaluatePlayerHandState import EvaluatePlayerHandState
            self.NextState = EvaluatePlayerHandState()
        elif(response == "s" or response == "S"):
            from EvaluateDealerHandState import EvaluateDealerHandState
            self.NextState = EvaluateDealerHandState()
        elif(response == "q" or response == "Q"):
            self.GameIsOver = True
        
        return self.NextState
