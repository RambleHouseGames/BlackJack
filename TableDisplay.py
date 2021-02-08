from GameData import GameData
from Clear import clear

def DisplayTable(HideDownCard, Message):
    gameData = GameData.getInstance() # get singleton reference

    clear() # clear the screen

    # SCORE BOARD
    print("=======================")
    print("| WINS: " + str(gameData.Wins) + " | LOSSES: " + str(gameData.Losses) + " |")
    print("=======================\n")

    #DEALER POINTS
    if(HideDownCard): # if the down card is hidden... 
        print("**** DEALER ***  " + str(gameData.DealerCards[0].GetPointValue()) + "\n") # only use the first card in the total
    else: # otherwise
        print("**** DEALER ***  " + str(gameData.GetDealerPoints()) + "\n") # add it up
    
    # there should only ever be a hidden down card while the dealer has exactly 2 cards, so we can do this manually
    if(HideDownCard):
        print(" =====   =====")
        print("|     | |*****|")
        print("| " + gameData.DealerCards[0].GetDisplayString() + " | |*****|") # get the Suit and Face character string from the card
        print("|     | |*****|")
        print(" =====   =====\n")
    else: # if the dealer down card is showing
        displayString = "" # we build this dynamic string because the dealer could have any number of cards
        for card in gameData.DealerCards:
            displayString += " =====  "
        displayString += "\n"
        for card in gameData.DealerCards:
            displayString += "|     | "
        displayString += "\n"
        for card in gameData.DealerCards:
            displayString += "| " + card.GetDisplayString() + " | "
        displayString += "\n"
        for card in gameData.DealerCards:
            displayString += "|     | "
        displayString += "\n"
        for card in gameData.DealerCards:
            displayString += " =====  "
        displayString += "\n"

        print(displayString) # print the dealers cards

    print(Message + "\n") # put the passed in message in the middle of the table

    displayString = "" # the player doesnt have down cards so we'll do thier cards dynamically every time
    for card in gameData.PlayerCards:
        displayString += " =====  "
    displayString += "\n"
    for card in gameData.PlayerCards:
        displayString += "|     | "
    displayString += "\n"
    for card in gameData.PlayerCards:
        displayString += "| " + card.GetDisplayString() + " | "
    displayString += "\n"
    for card in gameData.PlayerCards:
        displayString += "|     | "
    displayString += "\n"
    for card in gameData.PlayerCards:
        displayString += " =====  "
    displayString += "\n"

    print(displayString) # print the players cards

    print("***   YOU   ***  " + str(gameData.GetPlayerPoints())) # Show the players point total