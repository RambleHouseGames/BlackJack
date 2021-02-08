from enum import Enum
from random import seed
from random import randint
from datetime import datetime

Suite = Enum('Suite', 'CLUBS DIAMONDS HEARTS SPADES')
Face = Enum('Face', 'A 2 3 4 5 6 7 8 9 10 J Q K')

class Card:
    def __init__(self, suite, face):
        self.Suite = suite
        self.Face = face
        seed(datetime.now())

    def GetDisplayString(self):
        if(self.Suite == Suite.CLUBS):
            displayString = u'\u2663'
        elif(self.Suite == Suite.DIAMONDS):
            displayString = u'\u2666'
        elif(self.Suite == Suite.HEARTS):
            displayString = u'\u2665'
        elif(self.Suite == Suite.SPADES):
            displayString = u'\u2660'
        else:
            raise Exception("Unrecognized Suite: " + self.Suite)

        if(self.Face.name != '10'):
            displayString += ' '
        
        displayString += self.Face.name

        return displayString
    
    def GetPointValue(self):
        if(self.Face.name == 'A'):
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

class Shoe:
    __instance = None

    @staticmethod
    def getInstance():
        if(Shoe.__instance == None):
            Shoe()
        return Shoe.__instance

    def __init__(self):
        Shoe.__instance = self
        self.Cards = []

    def Reshuffle(self):
        self.Cards = []
        for suite in Suite:
            for face in Face:
                self.Cards.append(Card(suite, face))

    def DrawRandom(self):
        randIndex = randint(0, len(self.Cards) - 1)
        randCard = self.Cards[randIndex]
        del self.Cards[randIndex]
        return randCard
        

        
