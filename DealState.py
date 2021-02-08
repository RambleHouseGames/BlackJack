from Clear import clear
from GameData import GameData
from Shoe import Shoe

class DealState:
    def __init__(self):
        self.GameIsOver = False
        self.NextState = self

    def Update(self):
        shoe = Shoe.getInstance()
        gameData = GameData.getInstance()

        shoe.Reshuffle()
        gameData.SetPlayerStartingHand(shoe.DrawRandom(), shoe.DrawRandom())
        gameData.SetDealerStartingHand(shoe.DrawRandom(), shoe.DrawRandom())
        from EvaluatePlayerHandState import EvaluatePlayerHandState
        self.NextState = EvaluatePlayerHandState()
        return self.NextState
