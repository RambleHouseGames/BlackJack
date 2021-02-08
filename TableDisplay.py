from GameData import GameData
from Clear import clear

def DisplayTable(HideDownCard, Message):
    gameData = GameData.getInstance()

    clear()

    print("=======================")
    print("| WINS: " + str(gameData.Wins) + " | LOSSES: " + str(gameData.Losses) + " |")
    print("=======================\n")

    if(HideDownCard):
        print("**** DEALER ***  " + str(gameData.DealerCards[0].GetPointValue()) + "\n")
    else:
        print("**** DEALER ***  " + str(gameData.GetDealerPoints()) + "\n")
    
    if(HideDownCard):
        print(" =====   =====")
        print("|     | |*****|")
        print("| " + gameData.DealerCards[0].GetDisplayString() + " | |*****|")
        print("|     | |*****|")
        print(" =====   =====\n")
    else:
        displayString = ""
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

        print(displayString)

    print(Message + "\n")

    displayString = ""
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

    print(displayString)

    print("***   YOU   ***  " + str(gameData.GetPlayerPoints()))