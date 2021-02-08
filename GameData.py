import Shoe

class GameData:
    __instance = None

    @staticmethod
    def getInstance(): # do that singleton dance
        if(GameData.__instance == None):
            GameData()
        return GameData.__instance

    def __init__ (self):
        GameData.__instance = self
        self.DealerCards = [] # the dealers hand
        self.PlayerCards = [] # the players hand
        self.Wins = 0 # running total wins
        self.Losses = 0 # running total losses

    # drops any cards that the dealer was holding and starts the dealers hand with 2 cards
    def SetDealerStartingHand(self, card1, card2):
        self.DealerCards = [card1, card2]

    # drops any cards that the player was holding and starts the players hand with 2 cards
    def SetPlayerStartingHand(self, card1, card2):
        self.PlayerCards = [card1, card2]

    # used when the player hits
    def AddPlayerCard(self, card):
        self.PlayerCards.append(card)

    # used when the dealer hits
    def AddDealerCard(self, card):
        self.DealerCards.append(card)

    # Totals the players points
    def GetPlayerPoints(self):
        total = 0
        for card in self.PlayerCards:
            total += card.GetPointValue() # add up the face values
        
        if(total <= 21): # if the player is not busted then dont worry about soft aces
            return total

        # if the player is over 21 ... 
        for card in self.PlayerCards: # Iterate through all their cards ...
            if(card.Face.name == 'A'): # and when ever you find an ace ...
                total -= 10 # make the ace soft
                if(total <= 21): # and see if that got you under 21.  
                    return total # If it did, then use that as the total and stop looking for aces
        
        return total # other wise, sorry bro, you're busted

    # Totals the dealers points
    def GetDealerPoints(self):
        total = 0
        for card in self.DealerCards:
            total += card.GetPointValue() # add up the face values
        
        if(total <= 21): # if the dealer is not busted then dont worry about soft aces
            return total

        # if the dealer is over 21 ... 
        for card in self.DealerCards: # Iterate through all their cards ...
            if(card.Face.name == 'A'): # and when ever you find an ace ...
                total -= 10 # make the ace soft
                if(total <= 21): # and see if that got you under 21.
                    return total # If it did, then use that as the total and stop looking for aces
        
        return total # other wise, congratulations bro, the dealer busted
    
    # Adds Wins to the win counter
    def AddWins(self, count):
        self.Wins += count

    # Adds Losses to the loss counter
    def AddLosses(self, count):
        self.Losses += count
