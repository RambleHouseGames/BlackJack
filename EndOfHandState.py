from GameData import GameData
from TableDisplay import DisplayTable

class EndOfHandState:

    def __init__(self): # All States need these 2 properties
        self.GameIsOver = False
        self.NextState = self

    def Update(self):
        gameData = GameData.getInstance()
        message = ""

        if(gameData.GetPlayerPoints() > 21): # if the player busted... 
            gameData.AddLosses(1) # record the loss
            message = "BUST - YOU LOSE" # Let them know
        elif(gameData.GetDealerPoints() > 21): # if the dealer busted...
            gameData.AddWins(1) # record the win
            message = "DEALER BUSTS - YOU WIN" # Let them know
        elif(gameData.GetPlayerPoints() == gameData.GetDealerPoints()): # if its a push...
            message = "PUSH" # Dont record any wins or losses, and let them know
        elif(gameData.GetPlayerPoints() > gameData.GetDealerPoints()): # if none of that other stuff happened and the player is up...
            gameData.AddWins(1) # record the win
            message = "YOU WIN" # let them know
        elif(gameData.GetPlayerPoints() < gameData.GetDealerPoints()): # if none of that other stuff happened and the dealer is up...
            gameData.AddLosses(1) # record the loss
            message = "YOU LOSE" # let them know
        else:
            raise Exception("Unhandled Hand Outcome") # if I'm not as smart as I think I am, let me know

        message += " | (D)eal (Q)uit" # Append input options to message
        DisplayTable(False, message) # Draw Game Table with Dealer Down Card showing and the assembled message

        response = input("> ") # wait for input
        if(response == "d" or response == "D"): # If they want to play again
            from DealState import DealState
            self.NextState = DealState() # Get Set up for a new hand
        elif(response == "q" or response == "Q"): # If not
            self.GameIsOver = True # Break the main loop

        return self.NextState


        
