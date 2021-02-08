from enum import Enum
from random import seed
from random import randint
from datetime import datetime

Suite = Enum('Suite', 'CLUBS DIAMONDS HEARTS SPADES')
Face = Enum('Face', 'A 2 3 4 5 6 7 8 9 10 J Q K')

# represents one card in the deck
class Card:
    def __init__(self, suite, face):
        self.Suite = suite
        self.Face = face

    def GetDisplayString(self): # returns the unicode for the Suite and Face Value
        if(self.Suite == Suite.CLUBS):
            displayString = u'\u2663'
        elif(self.Suite == Suite.DIAMONDS):
            displayString = u'\u2666'
        elif(self.Suite == Suite.HEARTS):
            displayString = u'\u2665'
        elif(self.Suite == Suite.SPADES):
            displayString = u'\u2660'
        else:
            raise Exception("Unrecognized Suite: " + self.Suite) # Just incase someone draws the Ace of Horse Shoes

        if(self.Face.name != '10'): # 10 is the only on thats 2 characters long
            displayString += ' '
        
        displayString += self.Face.name

        return displayString
    
    # converts Face Values to integer point values.
    # I know it looks a little brute forcy but I think its the best option in this situation
    def GetPointValue(self):
        if(self.Face.name == 'A'): # Soft Aces are handled by GameData in the GetPlayerPoints and GetDealerPoints Methods
            return 11
        elif(self.Face.name == '2'):
            return 2
        elif(self.Face.name == '3'):
            return 3
        elif(self.Face.name == '4'):
            return 4
        elif(self.Face.name == '5'):
            return 5
        elif(self.Face.name == '6'):
            return 6
        elif(self.Face.name == '7'):
            return 7
        elif(self.Face.name == '8'):
            return 8
        elif(self.Face.name == '9'):
            return 9
        elif(self.Face.name == '10'):
            return 10
        elif(self.Face.name == 'J'):
            return 10
        elif(self.Face.name == 'Q'):
            return 10
        elif(self.Face.name == 'K'):
            return 10

# This is the Deck.  I called it a shoe incase I wanted to add multible decks later
class Shoe:
    __instance = None

    @staticmethod
    def getInstance(): # Do that singleton dance
        if(Shoe.__instance == None):
            Shoe()
        return Shoe.__instance

    def __init__(self):
        Shoe.__instance = self
        self.Cards = [] # cards go in here
        seed(datetime.now()) # seed the random number generator to time

    # Fills the Cards Array with a full deck (it doesn't randomize them, the randomness happens when they are drawn)
    def Reshuffle(self): 
        self.Cards = []
        for suite in Suite:
            for face in Face:
                self.Cards.append(Card(suite, face))

    # Removes a random card from the shoe and returns it
    def DrawRandom(self):
        randIndex = randint(0, len(self.Cards) - 1)
        randCard = self.Cards[randIndex]
        del self.Cards[randIndex]
        return randCard
        

        
