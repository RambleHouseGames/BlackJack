from Clear import clear
from GameData import GameData
from TableDisplay import DisplayTable

class EvaluatePlayerHandState:
    def __init__ (self):
        self.GameIsOver = False
        self.NextState = self

    def Update(self):
        gameData = GameData.getInstance()
        DisplayTable(True, "")
        self.GameIsOver = True
        if(gameData.GetPlayerPoints() == 21):
            from EvaluateDealerHandState import EvaluateDealerHandState
            self.NextState = EvaluateDealerHandState()
        elif(gameData.GetPlayerPoints() > 21):
            from EndOfHandState import EndOfHandState
            self.NextState = EndOfHandState()
        else:
            from PlayerInputState import PlayerInputState
            self.NextState = PlayerInputState()

        return self.NextState

