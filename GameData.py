import Shoe

class GameData:
    __instance = None

    @staticmethod
    def getInstance():
        if(GameData.__instance == None):
            GameData()
        return GameData.__instance

    def __init__ (self):
        GameData.__instance = self
        self.DealerCards = []
        self.PlayerCards = []
        self.Wins = 0
        self.Losses = 0

    def SetDealerStartingHand(self, card1, card2):
        self.DealerCards = [card1, card2]

    def SetPlayerStartingHand(self, card1, card2):
        self.PlayerCards = [card1, card2]

    def AddPlayerCard(self, card):
        self.PlayerCards.append(card)

    def AddDealerCard(self, card):
        self.DealerCards.append(card)

    def GetPlayerPoints(self):
        total = 0
        for card in self.PlayerCards:
            total += card.GetPointValue()
        
        if(total <= 21):
            return total

        for card in self.PlayerCards:
            if(card.Face.name == 'A'):
                total -= 10
                if(total <= 21):
                    return total
        
        return total

    def GetDealerPoints(self):
        total = 0
        for card in self.DealerCards:
            total += card.GetPointValue()
        
        if(total <= 21):
            return total

        for card in self.DealerCards:
            if(card.Face.name == 'A'):
                total -= 10
                if(total <= 21):
                    return total
        
        return total
    
    def AddWins(self, count):
        self.Wins += count

    def AddLosses(self, count):
        self.Losses += count
