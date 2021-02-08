from Clear import clear
from GameData import GameData
from Shoe import Shoe

class DealState:

    def __init__(self): # All States need these two properties
        self.GameIsOver = False
        self.NextState = self

    def Update(self):
        shoe = Shoe.getInstance() # Get the Singleton Reference
        gameData = GameData.getInstance() # Get the Singleton Reference

        shoe.Reshuffle() # Gives us a fresh deck
        gameData.SetPlayerStartingHand(shoe.DrawRandom(), shoe.DrawRandom()) # Player Gets 2 Cards
        gameData.SetDealerStartingHand(shoe.DrawRandom(), shoe.DrawRandom()) # Dealer Gets 2 Cards
        from EvaluatePlayerHandState import EvaluatePlayerHandState
        self.NextState = EvaluatePlayerHandState() # We Evaluate the players hand first because if the player has 21 there are no choices to be made.
        return self.NextState
