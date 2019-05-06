from random import shuffle
import Queue
class Card():
    def __init__(self, value, type):
        self.value = value
        self.type = type



def generateCards():
    cards = []
    for i in range(13):
        for j in range(4):
            cards.append(Card(i,j))
    
    shuffle(cards)

    deck = Queue.Queue()
    for i in range(len(cards)):
        deck.put(cards[i])
    
    return deck