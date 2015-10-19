# Testing template for the Card class

import random

# define globals for cards
SUITS = ['C', 'S', 'H', 'D']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K']
VALUES = {'A':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10}


#################################################
# Student should insert the implementation of the Card class here
class Card:
    def __init__(self, suit, rank):
        if (suit in SUITS) and (rank in RANKS):
            self.suit = suit
            self.rank = rank
        else:
            self.suit = None
            self.rank = None
            print "Invalid card: ", suit, rank

    def __str__(self):
        return self.suit + self.rank

    def get_suit(self):
        return self.suit

    def get_rank(self):
        return self.rank

    def draw(self, canvas, pos):
        card_loc = (CARD_CENTER[0] + CARD_SIZE[0] * RANKS.index(self.rank), 
                    CARD_CENTER[1] + CARD_SIZE[1] * SUITS.index(self.suit))
        canvas.draw_image(card_images, card_loc, CARD_SIZE, [pos[0] + CARD_CENTER[0], pos[1] + CARD_CENTER[1]], CARD_SIZE)
    
###################################################
# Test code

c1 = Card("S", "A")
print c1
print c1.get_suit(), c1.get_rank()
print type(c1)

c2 = Card("C", "2")
print c2
print c2.get_suit(), c2.get_rank()
print type(c2)

c3 = Card("D", "T")
print c3
print c3.get_suit(), c3.get_rank()
print type(c3)


###################################################
# Output to console

#SA
#S A
#<class '__main__.Card'>
#C2
#C 2
#<class '__main__.Card'>
#DT
#D T
#<class '__main__.Card'>