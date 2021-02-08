from TableDisplay import DisplayTable
from GameData import GameData
from Shoe import Shoe

class PlayerInputState:

    def __init__(self): # All States need these two properties
        self.GameIsOver = False
        self.NextState = self

    def Update(self):
        DisplayTable(True, "(H)it, (S)tand, (Q)uit") # Draw the table with the Dealer Down Card hidden and the Input Options as a message.
        response = input("> ") # Wait for input
        if(response == "h" or response == "H"):  # If the player Hits...
            gameData = GameData.getInstance()
            shoe = Shoe.getInstance()
            gameData.AddPlayerCard(shoe.DrawRandom()) # Give them a card
            from EvaluatePlayerHandState import EvaluatePlayerHandState
            self.NextState = EvaluatePlayerHandState() # See how that worked out for them
        elif(response == "s" or response == "S"): # If the player Stands...
            from EvaluateDealerHandState import EvaluateDealerHandState
            self.NextState = EvaluateDealerHandState() # Then its the dealers turn
        elif(response == "q" or response == "Q"): # If the player quits...
            self.GameIsOver = True # Break the main loop
        
        return self.NextState
