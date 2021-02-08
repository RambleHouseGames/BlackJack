from GameData import GameData
from TableDisplay import DisplayTable
from Shoe import Shoe

class EvaluateDealerHandState:
    def __init__ (self):
        self.GameIsOver = False
        self.NextState = self

    def Update(self):
        gameData = GameData.getInstance()
        shoe = Shoe.getInstance()
        DisplayTable(False, "DEALERS TURN")

        if(gameData.GetDealerPoints() >= 17):
            from EndOfHandState import EndOfHandState
            self.NextState = EndOfHandState()
        else:
            gameData.AddDealerCard(shoe.DrawRandom())

        return self.NextState