from GameData import GameData
from TableDisplay import DisplayTable

class EndOfHandState:
    def __init__(self):
        self.GameIsOver = False
        self.NextState = self

    def Update(self):
        gameData = GameData.getInstance()
        message = ""

        if(gameData.GetPlayerPoints() > 21):
            gameData.AddLosses(1)
            message = "BUST - YOU LOSE"
        elif(gameData.GetDealerPoints() > 21):
            gameData.AddWins(1)
            message = "DEALER BUSTS - YOU WIN"
        elif(gameData.GetPlayerPoints() == gameData.GetDealerPoints()):
            message = "PUSH"
        elif(gameData.GetPlayerPoints() > gameData.GetDealerPoints()):
            gameData.AddWins(1)
            message = "YOU WIN"
        elif(gameData.GetPlayerPoints() < gameData.GetDealerPoints()):
            gameData.AddLosses(1)
            message = "YOU LOSE"
        else:
            raise Exception("Unhandled Hand Outcome")

        message += " | (D)eal (Q)uit"
        DisplayTable(False, message)

        response = input("> ")
        if(response == "d" or response == "D"):
            from DealState import DealState
            self.NextState = DealState()
        elif(response == "q" or response == "Q"):
            self.GameIsOver = True

        return self.NextState


        
