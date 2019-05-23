from random import shuffle
import Queue
class Card():
    def __init__(self, number, type, value):
        self.number = number
        self.type = type
        self.value = value



def generateCards():
    cards = []
    value = 0
    for i in range(13):
        for j in range(4):
            cards.append(Card(i,j,value))
            value+=1
    
    shuffle(cards)

    deck = Queue.Queue()
    for i in range(len(cards)):
        deck.put(cards[i])
    
    return deck