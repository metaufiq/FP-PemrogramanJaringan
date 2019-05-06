class Player():
    def __init__(self, IP, conn):
        self.IP = IP
        self.conn = conn

    def setCards(self,cards):
        self.cards = cards
    
    def getCards(self):
        return self.cards
    
    