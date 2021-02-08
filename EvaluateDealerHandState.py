from GameData import GameData
from TableDisplay import DisplayTable
from Shoe import Shoe

class EvaluateDealerHandState:

    def __init__ (self): # All States need these 2 properties
        self.GameIsOver = False
        self.NextState = self

    def Update(self):
        gameData = GameData.getInstance() # get singleton reference
        shoe = Shoe.getInstance() # get singleton reference
        DisplayTable(False, "DEALERS TURN") # Draw the game table with Dealer Down Card Showing and a message
        # this is probably never going to be on the screen long enough for anyone to see, but hey might as well.

        if(gameData.GetDealerPoints() >= 17): # if the dealer is done ...
            from EndOfHandState import EndOfHandState
            self.NextState = EndOfHandState() # end the hand
        else: # otherwise
            gameData.AddDealerCard(shoe.DrawRandom()) # give him a card

        return self.NextState # if the dealer took a card, then the state doesn't change