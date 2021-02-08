from Clear import clear

class MainMenuState:
    def __init__(self):
        self.GameIsOver = False
        self.NextState = self

    def Update(self):
        clear()
        print("********************************")
        print("*** WELCOME TO QUINN LARSON'S **")
        print("***  SUPER AWESOME BLACKJACK  **")
        print("********************************\n")
        print("MENU\n")
        print("(N)ew Game")
        print("(E)xit")

        response = input("> ")
        if(response == 'E' or response == 'e'):
            self.GameIsOver = True
        elif(response == 'N' or response == "n"):
            from DealState import DealState
            self.NextState = DealState()
        return self.NextState