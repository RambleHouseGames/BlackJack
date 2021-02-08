from Clear import clear

class MainMenuState:

    def __init__(self): # All States Need these two properties
        self.GameIsOver = False
        self.NextState = self

    def Update(self):
        clear() # clear the screen
        print("********************************")
        print("*** WELCOME TO QUINN LARSON'S **")
        print("***  SUPER AWESOME BLACKJACK  **")
        print("********************************\n")
        print("MENU\n")
        print("(N)ew Game")
        print("(E)xit")

        response = input("> ") # get user Selection
        if(response == 'E' or response == 'e'):
            self.GameIsOver = True # Breaks the main loop and lets the process end
        elif(response == 'N' or response == "n"):
            from DealState import DealState
            self.NextState = DealState() # Instantiates a new DealState and returns it to the main loop to become the new CurrentState
        return self.NextState # If input was invalid, keep this state, update it again, and the user can try again