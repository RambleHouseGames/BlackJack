from Clear import clear
from GameData import GameData
from TableDisplay import DisplayTable

class EvaluatePlayerHandState:

    def __init__ (self): # All States need these two properties
        self.GameIsOver = False
        self.NextState = self

    def Update(self):
        gameData = GameData.getInstance() # Get Singleton Reference
        DisplayTable(True, "") # Draw the Game Table With the Dealer Down Card Hidden and No Message
        if(gameData.GetPlayerPoints() == 21): # If the player has 21...
            from EvaluateDealerHandState import EvaluateDealerHandState
            self.NextState = EvaluateDealerHandState() # skip player input and go to the dealers turn
        elif(gameData.GetPlayerPoints() > 21): # If the player is Busted...
            from EndOfHandState import EndOfHandState
            self.NextState = EndOfHandState() # End the hand
        else: # otherwise
            from PlayerInputState import PlayerInputState
            self.NextState = PlayerInputState() # The player has a decision to make

        return self.NextState

